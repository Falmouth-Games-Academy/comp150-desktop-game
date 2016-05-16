#include "stdafx.h"
#include "Room.h"


Room::Room()
{
}


Room::~Room()
{
}

void Room::addCell(std::shared_ptr<LevelCell> cell)
{
	containedCells.push_back(cell);
}