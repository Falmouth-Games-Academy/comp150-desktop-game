//! Class for the game.
/*!
  This class is used to manage, set up, and run the game.
  All game updates and SDL initialisations are performed here, 
  and the main game loop is begun here.
*/

#pragma once
#include "Texture.h"
#include "Level.h"

class PatientGame
{
public:

	//! Constructor for the game.
	/*!
	  The constructor should initialise the SDL subsystems
	*/
	PatientGame();

	//! Destructor for the game.
	/*!
	  The destructor should destroy the window and renderer,
	  as well as quitting SDL.
	*/
	~PatientGame();

	//! A method to start the game.
	/*!
	  This method should be called to begin the main game loop.
	*/
	void run();

	//! A public static member for storing window width.
	/*!
	   This is a static member for storing the width of the
	   window as an integer.
	*/
	static const int WINDOW_WIDTH = 1366;//1920;

	//! A public static member for storing window height.
	/*!
	  This is a static member for storing the height of the
	  window as an integer.
	*/
	static const int WINDOW_HEIGHT = 768;//1080;

	Texture* getGuardSprite() { return &guardSprite; }
	Texture* getDoctorSprite() { return &doctorSprite; }
	Texture* getCreatureSprite() { return &creatureSprite; }
	Texture* getPlayerSprite() { return &playerSprite; }
	Texture* getFloorSprite() { return &floorSprite; }
	Texture* getHorizontalWallSprite() { return &horizontalWallSprite;  }
	Texture* getVerticalWallSprite() { return &verticalWallSprite; }
	Texture* getHorizontalDoorSprite() { return &horizontalDoorSprite; }
	Texture* getVerticalDoorSprite() { return &verticalDoorSprite; }
	Texture* getExitSprite() { return &exitSprite; }

private:

	//! Pointer to the SDL window.
	/*!
	  This private member stores a pointer to the SDL window.
	  The window is initialised in the constructor.
	  Access the window through this.
	*/
	SDL_Window* window;

	//! Pointer to the SDL renderer.
	/*!
	  This private member stores a pointer to the SDL renderer.
	  The renderer is initialised in the constructor.
	  Access the renderer through this.
	*/
	SDL_Renderer* renderer;

	//! Private boolean to store whether the game is running.
	/*!
	  This is a boolean that stores whether the game is running or not.
	  It should be used to manage the main game loop.
	*/
	bool running;

	//! Private method to handle events.
	/*!
	  This method should be called in the main game loop to
	  handle events such as user input and quitting the game.
	*/
	void handleEvents();

	//! Private method to update the game state.
	/*!
	  This method should be called in the main game loop to
	  perform updates to the game state that must be done every
	  frame.
	*/
	void update();

	//! Private method to render to the screen.
	/*!
	  This method should be called in the main game loop to
	  update the renderer and display the updated screen.
	*/
	void render();

	//! Texture for the floor.
	/*!
	  This variable stores the texture that will be used
	  for the floor. It is initialised in the initialiser
	  list of the constructor.
	*/
	Texture floorSprite;
	Texture horizontalWallSprite;
	Texture verticalWallSprite;
	Texture horizontalDoorSprite;
	Texture verticalDoorSprite;
	Texture exitSprite;
	Texture guardSprite;
	Texture doctorSprite;
	Texture creatureSprite;
	Texture playerSprite;

	//! The current level.
	/*!
	  This stores the level that will be rendered.
	*/
	Level level;

	std::shared_ptr<Player> player;
	
};

