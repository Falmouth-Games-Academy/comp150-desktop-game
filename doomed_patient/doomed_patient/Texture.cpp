#include "stdafx.h"
#include "Texture.h"
#include "InitialisationError.h"

Texture::Texture(const std::string& fileName)
	: imageFilename(fileName), texture(nullptr)
{
	// Get the sprite size
	SDL_Surface* image;
	image = IMG_Load(imageFilename.c_str());

	if (!image)
	{
		throw InitialisationError("IMG_Load failed.");
	}

	spriteSizeX = image->w;
	spriteSizeY = image->h;
}


Texture::~Texture()
{
	if (texture)
		SDL_DestroyTexture(texture);
}

void Texture::loadTexture(SDL_Renderer* renderer)
{
	if (!texture)
	{
		texture = IMG_LoadTexture(renderer, imageFilename.c_str());

		if (!texture)
		{
			throw InitialisationError("IMG_LoadTexture failed");
		}
	}
}

void Texture::render(SDL_Renderer* renderer, int x, int y, int width, int height)
{
	loadTexture(renderer);

	// Rectangle that the texture will be loaded onto. x and y are its centre.
	SDL_Rect dest;
	dest.x = x - width / 2;
	dest.y = y - height / 2;
	dest.w = width;
	dest.h = height;
	SDL_RenderCopy(renderer, texture, nullptr, &dest);
}

 
