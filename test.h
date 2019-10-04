typedef struct 
{
	int x;
	char y;
	short z;
	double a;
	float b;
	int c;
	int d;
} my_int_t;

typedef struct 
{
	int x;
	char y;
	short z;
	double a;
	my_int_t my_int;
	float b;
	int c;
	int d;
} my_other_int_t;