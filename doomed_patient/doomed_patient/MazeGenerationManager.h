#pragma once
#include "Directions.h"
#include "LevelCell.h"
#include "Room.h"


class MazeGenerationManager
{
public:
	MazeGenerationManager();
	~MazeGenerationManager();

	std::vector<std::shared_ptr<LevelCell>> activeCells;
	std::shared_ptr<LevelCell> nextCell;
	Directions::Direction nextDirection;
	int currentIndex;

	VectorXY getNextCellCoordinates();
	std::shared_ptr<LevelCell> getPreviousCell();
	std::shared_ptr<LevelCell> getCurrentCell();
	std::shared_ptr<Room> getCurrentRoom();
	
};

