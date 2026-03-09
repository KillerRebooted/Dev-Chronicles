#include <stdio.h>

struct complex {
    float real;
    float imag;
};

int main()
{

    struct complex p1 = {2.0, 3.0};
    p1.real;
    struct complex *ptr = &p1;
    (*ptr).real;
    ptr->real;

    return 0;

}