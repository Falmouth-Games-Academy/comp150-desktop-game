#include "stdafx.h"
#include "CellPassage.h"
#include "Directions.h"
#include "PatientGame.h"


CellPassage::CellPassage(Directions::Direction direction, std::shared_ptr<LevelCell> cell, PatientGame* game)
	: CellEdge(direction, cell)
{
	initialiseSprite(game);
	initialisePosition();
}

CellPassage::~CellPassage()
{
}

void CellPassage::initialiseSprite(PatientGame* game)
{
		sprite = nullptr;
}
