#include "stdafx.h"
#include "LevelCell.h"
#include "PatientGame.h"
#include "Directions.h"
#include "CellWall.h"
#include "CellPassage.h"


LevelCell::LevelCell(PatientGame* game, int x, int y, std::shared_ptr<Room> room)
	: GameObject(game, game->getFloorSprite()),				// Call base class constructor
	gridPositionX(x),
	gridPositionY(y),
	room(room)
{
	// Calculate the window position from the grid position
	centreX = gridPositionX * spriteSizeX + spriteSizeX / 2;
	centreY = gridPositionY * spriteSizeY + spriteSizeY / 2;

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


void LevelCell::createWall(Directions::Direction direction)
{
	// shared_from_this() returns shared pointer to this
	edges[direction] = std::make_shared<CellWall>(direction, shared_from_this(), game);
}


void LevelCell::createPassage(Directions::Direction direction, bool isDoor)
{
	edges[direction] = std::make_shared<CellPassage>(direction, shared_from_this(), game, isDoor);
}