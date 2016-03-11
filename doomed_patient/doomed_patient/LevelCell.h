//! Class for the level's cells.
/*!
  This class manages the individual cells of a level.
  Each cell is responsible for creating its edges, and
  holds pointers to its edges. The cells also store their
  position in the grid.
*/

#pragma once
#include "GameObject.h"
#include "CellEdge.h"
#include "GridCoordinate.h"

class Room;

class LevelCell : public GameObject, public std::enable_shared_from_this<LevelCell>		// So that this can be passed as a shared pointer
{
public:
	//! Constructor for the level cell.
	/*!
	  This is the constructor for the level cells.
	  It takes a pointer to the game and an x and y
	  position. The constructor sets up the cell's 
	  window position based on its xy grid coordinates.
	  It also initialises the edges to nullptr.
	*/
	LevelCell(PatientGame* game, int x, int y, std::shared_ptr<Room> room);

	//! Creates a wall on a given side.
	/*!
	  This method instantiates and sets up a pointer to a CellWall
	  as the edge in the given direction relative to the cell.
	*/
	void createWall(Directions::Direction direction);

	//! Creates a passage on a given side.
	/*!
	This method instantiates and sets up a pointer to a CellPassage
	as the edge in the given direction relative to the cell.
	Passages may instead be doors, which is specified by the bool isDoor.
	*/
	void createPassage(Directions::Direction direction, bool isDoor);

	//! Render the cell.
	/*!
	This method renders the cell and all of its edges.
	*/
	void render(SDL_Renderer* renderer);

	//! Check if all edges are initialised.
	/*!
	  This method returns true if all edges have been instantiated,
	  that is, none of them are nullptr.
	*/
	bool allEdgesInitialised();

	//! Return a direction without an edge.
	/*!
	  This method returns a direction where an edge has not yet
	  been created.
	*/
	Directions::Direction getRandomUninitialisedDirection();

	//! Return the cell's coordinates.
	/*!
	  This getter returns the cell's coordinates as GridCoordinate.
	*/
	GridCoordinate getCoordinates() { return GridCoordinate(gridPositionX, gridPositionY); }

	std::shared_ptr<Room> room;

	//! The number of sides the cell has.
	/*!
	  This constant represents how many edges the 
	  cell has.
	*/
	static const int NUMBER_OF_SIDES = 4;


private:
	//! Cell's x position.
	/*!
	  This integer represents the cell's x 
	  coordinate on the level grid.
	*/
	int gridPositionX;

	//! Cell's y position.
	/*!
	This integer represents the cell's y
	coordinate on the level grid.
	*/
	int gridPositionY;

	//! A map containing the cell's edges.
	/*!
	  This map stores each of the cell's four edges.
	  The keys are the direction of the edge, and the values are
	  shared pointers to CellEdge.
	  The values for the four directions are initialised to nullptr
	  in the constructor.
	*/
	std::map<Directions::Direction, std::shared_ptr<CellEdge>> edges;
};

