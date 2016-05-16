#pragma once
#include "CellEdge.h"

class PatientGame;

class CellPassage :
	public CellEdge
{
public:
	//! Constructor for the CellPassafe.
	/*!
	This is the constructor for the cell passages. It calls back to the
	CellEdge constructor and also sets up the sprite and its window
	position for rendering.
	*/
	CellPassage(Directions::Direction direction, std::shared_ptr<LevelCell> cell, PatientGame* game);
	~CellPassage();

	//! This method returns whether the edge is a wall.
	/*!
	  This method returns a bool indicating whether the edge is a wall.
	  CellPassage is not a wall, so should return false.
	*/
	bool isWall() { return false; }
	
	//! This method returns whether the edge is a door.
	/*!
	This method returns a bool indicating whether the edge is a door.
	CellPassage is not a door, so should return true.
	*/
	bool isDoor() { return false; }

private:
	//! Initialises the sprite.
	/*!
	This method sets the sprite to the door sprite of
	the appropriate orientation, or nullptr if the edge
	is not a door.
	*/
	void initialiseSprite(PatientGame* game);

};

