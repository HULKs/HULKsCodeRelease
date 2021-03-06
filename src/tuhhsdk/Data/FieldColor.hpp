#pragma once

#include <cmath>

#include "Framework/DataType.hpp"
#include "Tools/Storage/Image.hpp"
#include "Tools/Storage/Image422.hpp"


class FieldColor : public DataType<FieldColor>
{
public:
  /// the name of this DataType
  DataTypeName name = "FieldColor";

  /// whether the field color is valid
  bool valid = false;

  /**
   * @brief Return how certain a pixel is fieldcolor. This std::function is
   * generated by the producing module. e.g. ChromaticityFieldColorDetection.cpp or
   * OneMeansFieldColorDetection.cpp
   * @return the probability how certain the pixel is field color
   */
  std::function<float(const YCbCr422& pixel)> isFieldColor;

  /**
   * @brief reset sets the field color to a defined state
   */
  void reset() override
  {
    valid = false;
  }

  void toValue(Uni::Value& value) const override
  {
    value = Uni::Value(Uni::ValueType::OBJECT);
    value["valid"] << valid;
  }

  void fromValue(const Uni::Value& value) override
  {
    value["valid"] >> valid;
  }
};
