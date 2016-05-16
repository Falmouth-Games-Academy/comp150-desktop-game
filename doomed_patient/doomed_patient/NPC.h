//! Class for the Guards.
/*!
This is a class for handling the Guards
and storing any unique data.
It inherits from th GameObject class
for any general data.
*/
#pragma once
#include "Character.h"
#include "VectorXY.h"
#include "Directions.h"
#include "LevelCell.h"
#include "Player.h"

class LevelCell;

class NPC : public Character
{
public:
	//!Constructor for the Guard
	/*!
	The constructor takes a pointer to the game and its
	starting grid coordinates.
	It calls through to the constructor for the base class,
	Character, and passes its sprite in.
	*/
	NPC(PatientGame* game, VectorXY startCoordinates, Texture* sprite);

	//! Moves the player.
	/*!
	This method moves the player in the specified
	direction at the player's speed.
	*/
	void move(Directions::Direction direction);

	virtual void update();

	virtual void changeSpriteDirection() = 0;

protected:
	
	Directions::Direction movementDirection;

private:

	// The cell the NPC is currently occupying.
	/*!
	This method updates the NPCs currentCell pointer to the
	cell that the game considers the NPC to be occupying.
	*/
	std::shared_ptr<LevelCell> currentCell;

	// Change the direction of the NPC.
	/*!
	  This method changes the direction of the NPC.
	*/
	void changeDirection();

	// Check if the NPC is in a position to change direction and change if so
	/*!
	  This method ensures that the NPC has passed the centre of the cell that
	  he is currently occupying before changing direction.
	  It calls changeDirection() if the NPC is past the centre and the edge is
	  a wall.
	*/
	void updateDirection();

	// Update the pointer to the cell the NPC is occupying
	/*!
	  This method updates the NPCs currentCell pointer to the
	  cell that the game considers the NPC to be occupying.
	  This method should be called before any other methods that
	  rely on cell position are called (i.e. movement/behaviour)
	*/
	void updateCurrentCell();
};
