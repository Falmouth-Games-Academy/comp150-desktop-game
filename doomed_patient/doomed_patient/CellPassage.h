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
	CellPassage(Directions::Direction direction, std::shared_ptr<LevelCell> cell, PatientGame* game, bool isDoor);
	~CellPassage();

	//! Defines whether the passage is a door.
	/*!
	  If this boolean is true, the passage will be rendered
	  as a door instead.
	*/
	bool isDoor;

private:
	//! Initialises the sprite.
	/*!
	This method sets the sprite to the door sprite of
	the appropriate orientation, or nullptr if the edge
	is not a door.
	*/
	void initialiseSprite(PatientGame* game);

};

