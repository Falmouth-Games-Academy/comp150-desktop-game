#include "stdafx.h"
#include "Level.h"
#include "GridCoordinate.h"
#include "Directions.h"
#include "LevelCell.h"
#include "Room.h"
#include "Exit.h"
#include "Guard.h"
#include "Doctor.h"
#include "Player.h"

Level::Level(PatientGame* game)
	:cells(GRID_SIZE_X, std::vector<std::shared_ptr<LevelCell>>(GRID_SIZE_Y, nullptr)),		// Initialise vector to correct size
	game(game)
{
}


Level::~Level()
{
	
}
 

bool Level::containsCoordinates(GridCoordinate coordinates)
{
	// Check if given coordinates are within the level size
	return (0 <= coordinates.x && coordinates.x < GRID_SIZE_X && 0 <= coordinates.y && coordinates.y < GRID_SIZE_Y);
}


std::shared_ptr<LevelCell> Level::getCell(GridCoordinate coordinates)
{
	return cells[coordinates.x][coordinates.y];
}


std::shared_ptr<Room> Level::createRoom()
{
	// Create a room and add a pointer to it to the vector of rooms
	std::shared_ptr<Room> room = std::make_shared<Room>();
	rooms.push_back(room);
	return room;
}

void Level::createGuard()
{
	// Create a guard and add a pointer to the vector of guards
	// Indicates the position of the guards
	int guardPosX = rand() % GRID_SIZE_X;
	int guardPosY = rand() % GRID_SIZE_Y;

	GridCoordinate guardCoords(guardPosX, guardPosY);
	std::shared_ptr<Guard>guard = std::make_shared<Guard>(game, getCell(guardCoords));

	npc.push_back(guard);
}

void Level::createDoctor()
{
	// Create a doctor and add a pointer to the vector of doctors
	// Indicates the position of the doctors
	int doctorPosX = rand() % GRID_SIZE_X;
	int doctorPosY = rand() % GRID_SIZE_Y;

	GridCoordinate doctorCoords(doctorPosX, doctorPosY);
	std::shared_ptr<Doctor>doctor = std::make_shared<Doctor>(game, getCell(doctorCoords));

	npc.push_back(doctor);
}

std::shared_ptr<Player> Level::createPlayer()
{
	// Create a guard and add a pointer to the vector of player
	GridCoordinate playerCoords(Player::playerStartX, Player::playerStartY);
	player = std::make_shared<Player>(game, getCell(playerCoords));
	return player;
}


void Level::generateCells(std::vector<std::shared_ptr<LevelCell>>& activeCells)
{
	// Last index. Can be changed (first, middle, or random) to give different results
	int currentIndex = activeCells.size() - 1;
	std::shared_ptr<LevelCell> currentCell = activeCells[currentIndex];

	// Delete the cell from the list of active cell if all edges have been set
	if (currentCell->allEdgesInitialised())
	{
		activeCells.erase(activeCells.begin() + currentIndex);
		return;
	}

	// Get a random direction that doesn't yet have an edge set
	Directions::Direction randomDirection = currentCell->getRandomUninitialisedDirection();

	// Calculate the next coordinates to be visited
	GridCoordinate nextCellCoordinates = currentCell->getCoordinates() + Directions::getDirectionVector(randomDirection);

	if (containsCoordinates(nextCellCoordinates))
	{
		std::shared_ptr<LevelCell> nextCell = getCell(nextCellCoordinates);

		// If there isn't a cell in the visted coordinates, create the cell and a passage
		if (!nextCell)
		{
			// Decide if the passaage will be a door by picking random number between 0 and 1
			double randomNumber = static_cast<double>(rand()) / static_cast<double>(RAND_MAX);
			bool isDoor = (randomNumber < DOOR_PROBABILITY) ? true : false;

			currentCell->createPassage(randomDirection, isDoor);

			// nextCell is in a new room if there is a door, otherwise it's in the same room
			if (isDoor)
			{
				nextCell = createCell(nextCellCoordinates, createRoom());
			}
			else
			{
				nextCell = createCell(nextCellCoordinates, currentCell->room);
			}

			nextCell->createPassage(Directions::getOpposite(randomDirection), isDoor);

			// Add new cell to list of active cells
			activeCells.push_back(nextCell);
		}
		// If a cell already exists and it's in the same room, create a passage
		else if (currentCell->room == nextCell->room)
		{
			currentCell->createPassage(randomDirection, false);
			nextCell->createPassage(Directions::getOpposite(randomDirection), false);
		}
		// If a cell already exists and isn't in the same room, create a wall
		else
		{
			currentCell->createWall(randomDirection);
			nextCell->createWall(Directions::getOpposite(randomDirection));
		}
	}
	// If the current cell is at the edge of the level, create a wall
	else
	{
		currentCell->createWall(randomDirection);
	}
}


void Level::placeExit()
{
	// Get random 0 or 1. Edge is on right if not on top
	bool exitOnTopEdge = rand() % 2;

	int exitPosX;
	int exitPosY;
    
	if (exitOnTopEdge)
	{
		exitPosX = rand() % GRID_SIZE_X;
		exitPosY = 0;
	}
	else
	{
		exitPosX = GRID_SIZE_X - 1;
		exitPosY = rand() % GRID_SIZE_Y;
	}

	GridCoordinate exitCoords(exitPosX, exitPosY);
	exit = std::make_shared<Exit>(game, getCell(exitCoords));
}


void Level::generateMaze()
{
	// Randomly choose position to start from and add it to activeCells
	std::vector<std::shared_ptr<LevelCell>> activeCells;
	std::shared_ptr<Room> room = createRoom();
	GridCoordinate firstCellCoordinates = getRandomCoordinates();
	std::shared_ptr<LevelCell> firstCell = createCell(firstCellCoordinates, room);
	activeCells.push_back(firstCell);

	while (activeCells.size() > 0)
	{
		generateCells(activeCells);

		// For testing
		//render(renderer);
		//SDL_RenderPresent(renderer);
	}
	
	placeExit();
	createGuard();
	createDoctor();
}


void Level::render(SDL_Renderer* renderer)
{
	for (int x = 0; x < GRID_SIZE_X; x++)
	{
		for (int y = 0; y < GRID_SIZE_Y; y++)
		{
			// Render each cell
			if (cells[x][y])
			{
				cells[x][y]->render(renderer);
			}
		}
	}

	exit->render(renderer);
	for (int i = 0; i < npc.size(); i++)
	{
		npc[i]->render(renderer);
	}
	player->render(renderer);
}


std::shared_ptr<LevelCell> Level::createCell(GridCoordinate coordinates, std::shared_ptr<Room> room)
{
	cells[coordinates.x][coordinates.y] = std::make_shared<LevelCell>(game, coordinates.x, coordinates.y, room);
	return cells[coordinates.x][coordinates.y];
}


GridCoordinate Level::getRandomCoordinates()
{
	GridCoordinate coordinates;
	coordinates.x = rand() % Level::GRID_SIZE_X;
	coordinates.y = rand() % Level::GRID_SIZE_Y;
	return coordinates;
}