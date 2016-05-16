#include "stdafx.h"
#include "LevelCell.h"
#include "PatientGame.h"
#include "Directions.h"
#include "CellWall.h"
#include "CellPassage.h"
#include "Room.h"

LevelCell::LevelCell(PatientGame* game, VectorXY coordinates)
	: GameObject(game, game->getFloorSprite()),				// Call base class constructor
	gridPosition(coordinates)
{
	// Calculate the window position from the grid position
	centre = gridPosition.convertGridToWindow();

	// Set up empty edges
	edges[Directions::Direction::NORTH] = nullptr;
	edges[Directions::Direction::EAST] = nullptr;
	edges[Directions::Direction::WEST] = nullptr;
	edges[Directions::Direction::SOUTH] = nullptr;
}

LevelCell::LevelCell(PatientGame* game, VectorXY coordinates, Texture* sprite)
	: GameObject(game, sprite),				// Call base class constructor
	gridPosition(coordinates)
{
	// Calculate the window position from the grid position
	centre = gridPosition.convertGridToWindow();

	// Set up empty edges
	edges[Directions::Direction::NORTH] = nullptr;
	edges[Directions::Direction::EAST] = nullptr;
	edges[Directions::Direction::WEST] = nullptr;
	edges[Directions::Direction::SOUTH] = nullptr;
}


void LevelCell::render(SDL_Renderer* renderer)
{
	// Render the cell
	GameObject::render(renderer);

	// Iterate through all map elements and render each edge
	for (auto& element : edges)
	{
		std::shared_ptr<CellEdge> edge = element.second;
		if (edge)
			edge->render(renderer);
	}
}


bool LevelCell::allEdgesInitialised()
{
	// Iterate through all map elements and check if edge exists
	for (auto& element : edges)
	{
		std::shared_ptr<CellEdge> edge = element.second;
		if (!edge)
		{
			return false;
		}
	}
	return true;
}


Directions::Direction LevelCell::getRandomUninitialisedDirection()
{
	std::vector<Directions::Direction> uncheckedDirections = {Directions::Direction::NORTH, Directions::Direction::EAST, 
															  Directions::Direction::WEST, Directions::Direction::SOUTH};

	for (;;)
	{
		int index = rand() % (uncheckedDirections.size());

		if (!edges[uncheckedDirections[index]])
		{
			return uncheckedDirections[index];
		}
		else
		{
			uncheckedDirections.erase(uncheckedDirections.begin() + index);
		}
	}
}


Directions::Direction LevelCell::getBiasedUninitialisedDirection(Directions::Direction direction)
{
	if (!edges[direction])
	{
		return direction;
	}
	else
	{
		return getRandomUninitialisedDirection();
	}
}


void LevelCell::assignRoom(std::shared_ptr<Room> assignedRoom)
{
	room = assignedRoom;
	std::shared_ptr<Room> cellRoom = room.lock();
	cellRoom->addCell(shared_from_this());
}