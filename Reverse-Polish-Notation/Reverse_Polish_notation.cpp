#include <math.h>
#include <vector>
#include "calc.h"

#include <iostream>
using namespace std;

#define what_is(x) cerr << #x << " = " << (x) << endl;

node::node(char ch) : isop(true), operation(ch), number(0.0f){}
node::node(double num) : isop(false), operation('$'), number(num){}

bool torpn::isDelim(char ch){
    return ch == ' ';
}

bool torpn::isOperation(char ch){
    return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '#';
}

bool torpn::isNum(char ch){
    return ch == '.' || (ch >= '0' && ch <= '9');
}

bool torpn::isUnary(char ch){
    return ch == '+' || ch == '-';
}

int torpn::priority(char op) {
    return
        op == '#' ? 3 :
        op == '+' || op == '-' ? 1 :
        op == '*' || op == '/' ? 2 :
        -1;
}

vector<node> torpn::str_to_rpn(string s){
    s = '(' + s + ')';
    vector<node> rpn;
    vector<char> op;
    double sign = 1.0f;

    for(int i = 0; i < s.length(); i++){
        if (isDelim(s[i])) continue;
        if (s[i] == '('){
            op.push_back('(');
            continue;
        }
        if (s[i] == ')'){
            while(op.size()){
                char top = op.back(); op.pop_back();
                if (top == '(') break;
                rpn.push_back(node(top));
            }
            continue;
        }
        if (isUnary(s[i]) && s[i - 1] == '('){
            continue;
        }
        if (isOperation(s[i])){
            while(op.size() && priority(op.back()) >= priority(s[i])){
                rpn.push_back(node(op.back()));
                op.pop_back();
            }
            op.push_back(s[i]);
            continue;
        }
        string operand;
        if (i - 2 >= 0  && s[i - 2] == '(' 
            && 
            (s[i - 1] == '-' || s[i - 1] == '+')) operand += '-';
        while(i < s.length() && isNum(s[i])) operand += s[i++];
        --i;

        std::size_t error;
        double numb = std::stod(operand, &error);
        rpn.push_back(node(numb));
    }

    return rpn;
}

double calc::calculate(string str){
    vector<node> rpn = torpn::str_to_rpn(str); 
    vector<double> value_stack;

    what_is(rpn.size());
    for(int i = 0; i < rpn.size(); i++){
        if (rpn[i].isop){
            double result;
            if (rpn[i].operation == '#'){
                double operand = value_stack.back(); value_stack.pop_back();
                result = exp(operand);
            }
            else{
                double r = value_stack.back(); value_stack.pop_back();
                double l = value_stack.back(); value_stack.pop_back();
                switch(rpn[i].operation){
                    case '+':
                        result = l + r; break;
                    case '-':
                        result = l - r; break;
                    case '*':
                        result = l * r; break;
                    case '/':
                        result = l / r; break;
                }
            }
            value_stack.push_back(result);
        }
        else value_stack.push_back(rpn[i].number);
    }
    return value_stack[0];
}
