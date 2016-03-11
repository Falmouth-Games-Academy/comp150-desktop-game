#include "stdafx.h"
#include "GridCoordinate.h"


GridCoordinate::GridCoordinate()
{
}

GridCoordinate::GridCoordinate(int x, int y)
	:x(x), y(y)
{
}


GridCoordinate::~GridCoordinate()
{
}

GridCoordinate GridCoordinate::operator+(const GridCoordinate& otherCoord)
{
	GridCoordinate newCoordinates(x + otherCoord.x, y + otherCoord.y);
	return newCoordinates;
}