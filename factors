#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <inttypes.h>

unsigned long long int factors(unsigned long long int number);
int main (int argc, char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Not the right Usage.\n");
        return (0);
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
        fprintf(stderr, "Error: can't open file %s\n", argv[1]);

    char buffer[256];
    unsigned long long int number, first, second;
    while (fgets(buffer, 256, file) != NULL)
    {
        number = atoi(buffer);
        first = factors(number);
        if (first == 0)
        {
            printf("Couldn't factorize %lld\n", number);
            continue;
        }
        printf("%lld=%lld*%lld\n", number, number/first, first);
    }
    fclose(file);
    return (0);
}

unsigned long long int factors(unsigned long long int number)
{
    unsigned long long int i;
    for (i = 2; i < number; i++)
    {
        if (number % i != 0)
        {
            continue;
        }
        return (i);
    }
    return (0);
}
