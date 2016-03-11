#pragma once
#include "CellEdge.h"
#include "Directions.h"

class PatientGame;

class CellWall :
	public CellEdge
{
public:
	//! Constructor for the CellWall.
	/*!
	This is the constructor for the cell walls. It calls back to the
	CellEdge constructor and also sets up the sprite and its window
	position for rendering.
	*/
	CellWall(Directions::Direction direction, std::shared_ptr<LevelCell> cell, PatientGame* game);
	~CellWall();


private:
	//! Initialises the sprite.
	/*!
	  This method sets the sprite to the wall sprite of
	  the appropriate orientation.
	*/
	void initialiseSprite(PatientGame* game);
};

