#include "stdafx.h"
#include "CellPassage.h"
#include "Directions.h"
#include "PatientGame.h"


CellPassage::CellPassage(Directions::Direction direction, std::shared_ptr<LevelCell> cell, PatientGame* game, bool isDoor)
	: CellEdge(direction, cell),
	isDoor(isDoor)
{
	initialiseSprite(game);
	initialisePosition();
}


CellPassage::~CellPassage()
{
}



void CellPassage::initialiseSprite(PatientGame* game)
{
	if (isDoor)
	{
		if (direction == Directions::Direction::NORTH || direction == Directions::Direction::SOUTH)
		{
			sprite = game->getHorizontalDoorSprite();
		}

		else if (direction == Directions::Direction::EAST || direction == Directions::Direction::WEST)
		{
			sprite = game->getVerticalDoorSprite();
		}
	}
	else
	{
		sprite = nullptr;
	}
}
	
