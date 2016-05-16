#include "stdafx.h"
#include "Level.h"
#include "Directions.h"
#include "LevelCell.h"
#include "Room.h"
#include "Exit.h"
#include "Guard.h"
#include "Doctor.h"
#include "Player.h"
#include "PatientGame.h"
#include "Maze.h"

const VectorXY Level::PLAYER_START(0, Level::GRID_SIZE_Y - 1);

Level::Level(PatientGame* game)	
	:game(game)
{
}


Level::~Level()
{
}


bool Level::containsCoordinates(VectorXY coordinates)
{
	// Check if given coordinates are within the level size
	return (0 <= coordinates.x && coordinates.x < GRID_SIZE_X && 0 <= coordinates.y && coordinates.y < GRID_SIZE_Y);
}


std::shared_ptr<LevelCell> Level::getCell(VectorXY coordinates)
{
	return maze->getCell(coordinates);
}


bool Level::positionOccupied(VectorXY coordinates)
{
	for each (std::shared_ptr<Character> npc in characters)
	{
		if (coordinates == npc->getStartCoordinates())
		{
			return true;
		}
	}
	return false;
}


template<typename CharacterType>
std::shared_ptr<CharacterType> Level::createCharacter(VectorXY startCoordinates)
{
	std::shared_ptr<CharacterType> character = std::make_shared<CharacterType>(game, startCoordinates);
	characters.push_back(character);
	return character;
}


void Level::placeExit()
{
	// Get random 0 or 1. Edge is on right if not on top
	bool exitOnTopEdge = rand() % 2;

	VectorXY exitCoords;
    
	if (exitOnTopEdge)
	{
		exitCoords.x = rand() % GRID_SIZE_X;
		exitCoords.y = 0;
	}
	else
	{
		exitCoords.x = GRID_SIZE_X - 1;
		exitCoords.y = rand() % GRID_SIZE_Y;
	}

	exit = std::make_shared<Exit>(game, exitCoords);
}

void Level::clearLevel()
{
	maze = std::make_unique<Maze>(game);

	characters.clear();
}

void Level::generateMaze()
{
	clearLevel();

	maze->generate();
	
	placeExit();

	player = createCharacter<Player>(PLAYER_START);

	// Temporary literal 5 for testing
	for (int i = 0; i < 20; i++)
	{
		createCharacter<Guard>(getUnoccupiedRandomCoords());
		createCharacter<Doctor>(getUnoccupiedRandomCoords());
	}
}


void Level::render(SDL_Renderer* renderer)
{
	maze->render(renderer);

	exit->render(renderer);

	for (int i = 0; i < characters.size(); i++)
	{
		characters[i]->render(renderer);
	}
}


VectorXY Level::getUnoccupiedRandomCoords()
{
	bool positionIsValid = false;

	VectorXY unoccupiedCoordinates(rand() % GRID_SIZE_X, rand() % GRID_SIZE_Y);

	if (!characters.empty())
	{	
		// Ensure that 2 NPCs aren't spawned in the same place
		while (positionOccupied(unoccupiedCoordinates))
		{
			unoccupiedCoordinates.x = rand() % GRID_SIZE_X;
			unoccupiedCoordinates.y = rand() % GRID_SIZE_Y;
		}
	}

	return unoccupiedCoordinates;
}

VectorXY Level::getRandomCoordinates()
{
	VectorXY coordinates;
	coordinates.x = rand() % Level::GRID_SIZE_X;
	coordinates.y = rand() % Level::GRID_SIZE_Y;
	return coordinates;
}