#pragma once
#include "VectorXY.h"
#include "Room.h"
#include "MazeGenerationManager.h"

class LevelCell;
class Room;
class PatientGame;

class Maze
{
public:
	Maze(PatientGame* game);
	~Maze();

	//! Generates the maze.
	/*!
	  This method begins the maze generation process.
	*/
	void generate();

	//! Render the maze.
	/*!
	  This method renders the cells in the maze.
	*/
	void render(SDL_Renderer* renderer);

	//! Returns the cell at the given coordinates.
	/*!
	  This method returns a pointer to the cell located
	  at the given coordinates.
	*/
	std::shared_ptr<LevelCell> getCell(VectorXY coordinates);

	//! Size of each level cell.
	/*!
	  This static member represents the size of each
	  cell of the level, which corresponds to the size of
	  the sprite. Used to convert grid coordinates to
	  window coordinates and vice versa.
	*/
	static const int CELL_SIZE = 64;

private:
	//! Generate the maze cells.
	/*!
	  This method implements the Growing Tree Algorithm to
	  generate each cell of the level and the positionings
	  of walls and doors.
	*/
	void generateCells(MazeGenerationManager& generationManager);

	//! Check if the given coordinates are in the level.
	/*!
	  This method checks if the given coordinates are contained
	  in the level. If so, it returns true.
	*/
	bool containsCoordinates(VectorXY coordinates);

	//! Create a cell.
	/*!
	  This method created a cell at the given grid coordinates in the
	  given room. It returns a pointer to the cell it has created.
	*/
	std::shared_ptr<LevelCell> createCell(VectorXY coordinates, std::shared_ptr<Room> room);

	//! Create a room.
	/*!
	  This method creates a room and returns a pointer to the
	  room it has created. Rooms are used to determine where
	  passages should be placed instead of walls.
	  The room is set as a corridor if it came from a non-corridor,
	  and a non-corridor if it came from a corridor.
	*/
	std::shared_ptr<Room> createRoom(std::shared_ptr<Room> cameFrom);

	//! Create a room.
	/*!
	  This method creates a room and returns a pointer to the
	  room it has created. Rooms are used to determine where
	  passages should be placed instead of walls.
	  This version of the method should be used when the very
	  first cell is created.
	*/
	std::shared_ptr<Room> createRoom();

	//! Returns random coordinates.
	/*!
	  This method returns random grid coordinates that
	  are contained in the level.
	*/
	VectorXY getRandomCoordinates();

	//! Vector that holds pointers to the level's cells.
	/*!
	  This private 2d vector holds pointers to the level's
	  cells. The cells are instantiated and added to the
	  vector when generate is called.
	*/
	std::vector<std::vector<std::shared_ptr<LevelCell>>> cells;

	//! Pointer to the game
	/*!
	  This is a pointer to the game, that is used to pass
	  to the generated cells so that they can access their
	  sprite.
	*/
	PatientGame* game;

	//! Vector of rooms.
	/*!
	  This vector stores pointers to all rooms that have been
	  created using createRoom().
	*/
	std::vector<std::shared_ptr<Room>> rooms;

	bool assignDoor(MazeGenerationManager& generationManager);

	void createCellInNewRoom(MazeGenerationManager& generationManager);
	void createCellInSameRoom(MazeGenerationManager& generationManager);
	void createPassage(MazeGenerationManager& generationManager);
	void createWall(MazeGenerationManager& generationManager);



	//! The probability that a door will be made.
	/*!
	  This constant defines the probability that a door
	  will be made instead of a passage. This value should
      be between 0 and 1.
      0 means that doors will never spawn, 1  means that
      doors will always spawn.
	*/
	const double DOOR_PROBABILITY = 0.03;

	const int MIN_ROOM_SIZE = 15;
	const int MAX_ROOM_SIZE = 30;
};

