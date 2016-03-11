#pragma once

class GridCoordinate
{
public:
	GridCoordinate();
	GridCoordinate(int x, int y);
	~GridCoordinate();
	int x;
	int y;
	
	GridCoordinate operator+(const GridCoordinate& otherCoord);

};