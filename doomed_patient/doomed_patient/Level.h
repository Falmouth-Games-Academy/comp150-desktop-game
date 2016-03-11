//! Class for the level.
/*!
  This class stores data about the level and
  manages the level generation process.
*/

#pragma once
#include "GridCoordinate.h"

class Room;
class LevelCell;
class PatientGame;
class Exit;
class Guard;
class Doctor;
class GameObject;
class Player;

class Level
{
public:
	//! Constructor for the level.
	/*!
	  This is the constructor for the level. It takes a pointer
	  to the game to initialise that field, and also initialises the
	  vector of cells to contain nullptr.
	*/
	Level(PatientGame* game);

	//! Destructor for the level.
	/*!
	  The destructor deletes the cells that the cells
	  vector points to.
	*/
	~Level();

	//! Generates the level.
	/*!
	  This method begins the level generation process.
	*/
	void generateMaze();

	//! Render the level.
	/*!
	This method renders the cells in the level and the exit.
	*/
	void render(SDL_Renderer* renderer);

	//! Returns the cell at the given coordinates.
	/*!
	This method returns a pointer to the cell located
	at the given coordinates.
	*/
	std::shared_ptr<LevelCell> getCell(GridCoordinate coordinates);

	//! Width of the level.
	/*!
	  This static member represents the width of
	  the level in grid squares as an integer.
	*/
	static const int GRID_SIZE_X = 21;

	//! Height of the level.
	/*!
	This static member represents the height of
	the level in grid squares as an integer.
	*/
	static const int GRID_SIZE_Y = 12;
	
	// For testing
	SDL_Renderer* renderer;

	std::shared_ptr<Player> createPlayer();


private:
	//! Generate the maze cells.
	/*!
	  This method implements the Growing Tree Algorithm to
	  generate each cell of the level and the positionings 
	  of walls and doors.
	*/
	void generateCells(std::vector<std::shared_ptr<LevelCell>>& activeCells);

	//! Check if the given coordinates are in the level.
	/*!
	  This method checks if the given coordinates are contained
	  in the level. If so, it returns true.
	*/
	bool containsCoordinates(GridCoordinate coordinates);

	//! Create a cell.
	/*!
	  This method created a cell at the given grid coordinates in the
	  given room. It returns a pointer to the cell it has created.
	*/
	std::shared_ptr<LevelCell> createCell(GridCoordinate coordinates, std::shared_ptr<Room> room);

	//! Create a room.
	/*!
	  This method creates a room and returns a pointer to the
	  room it has created. Rooms are used to determine where
	  passages should be placed instead of walls.
	*/
	std::shared_ptr<Room> createRoom();

    //! Returns random coordinates.
	/*!
	  This method returns random grid coordinates that
	  are contained in the level.
	*/
	GridCoordinate getRandomCoordinates();

	//! Add the exit to the level.
	/*!
	  This method creates an instance of the exit and
	  sets its position to a random place on the top or
	  left edge.
	*/
	void placeExit();

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

	//! Pointer to the exit.
	/*!
	This is a shared pointer to the exit of the level.
	The exit is of type Exit, and is created and placed
	during the level generation process.
	*/
	std::shared_ptr<Exit> exit;

	//! The probability that a door will be made.
	/*!
	  This constant defines the probability that a door
	  will be made instead of a passage. This value should
	  be between 0 and 1.
	  0 means that doors will never spawn, 1  means that 
	  doors will always spawn.
	*/
	const double DOOR_PROBABILITY = 0.03;

	//! Add the Guards and Doctors to the level.
	/*!
	This method creates an instance of the Guards/Doctors and
	sets its position to a random place on the map.
	*/
	std::vector<std::shared_ptr<GameObject>> npc;
	void createGuard();
	void createDoctor();

	std::shared_ptr<Player> player;
	
};

