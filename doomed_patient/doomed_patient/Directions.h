#pragma once
#include "GridCoordinate.h"

class Directions
{
public:

	//! Enum class for the four directions.
	/*!
	  This enum class is used to represent the
	  four directions, north, south, east and west.
	*/
	enum class Direction
	{
		NORTH,
		EAST,
		SOUTH,
		WEST
	};

	Directions();
	~Directions();

	static GridCoordinate getDirectionVector(Direction direction);
	static Direction getOpposite(Direction direction);
};

