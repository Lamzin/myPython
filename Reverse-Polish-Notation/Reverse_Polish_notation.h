#pragma once

#include <string>
#include <vector>

using namespace std;

struct node{
	bool isop;
	char operation;
	double number;

	node(char ch);
	node(double num);
};

class torpn{
private:
	static bool isDelim(char ch);
	static bool isOperation(char ch);
	static bool isNum(char ch);
	static bool isUnary(char ch);
	static int priority(char op);

public:
	static vector<node> str_to_rpn(string s);
};

class calc{
public:
	double calculate(string str);
};
