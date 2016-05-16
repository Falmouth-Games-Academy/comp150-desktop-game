#pragma once


class LevelCell;

class Room
{
public:
	Room();
	~Room();
	bool corridor;
	std::vector<std::shared_ptr<LevelCell>> getCells() { return containedCells; }
	void addCell(std::shared_ptr<LevelCell> cell);

private:
	std::vector<std::shared_ptr<LevelCell>> containedCells;
};

