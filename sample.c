#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>


void write_pixel(int x, int y, short colour)
{
    volatile short *vga_addr = (volatile short *)(0x08000000 + (y << 10) + (x << 1)); // address of pixel
    *vga_addr = colour;                                                               // pixel value
}

void write_char(int x, int y, char c)
{
    volatile char *character_buffer = (char *)(0x09000000 + (y << 7) + x);
    *character_buffer = c;
}
void clear_screen()
{
    int x, y;
    for (x = 0; x < 320; x++)
    {
        for (y = 0; y < 240; y++)
        {
            write_pixel(x, y, 0);
        }
    }
}

void clear_screen_char()
{
    int x, y;
    for (x = 0; x < 80; x++)
    {
        for (y = 0; y < 60; y++)
        {
            write_char(x, y, 0);
        }
    }
}

int random_int(int min, int max)
{
    return min + rand() % (max - min + 1);
}

int a = 0;
int b = 1;
int c;

int main()
{
    for (int i = 0; i < 30; i++)
    {
        c = a + b;
        srand(i); // seeding with i
        int x = random_int(0, 75);
        int y = random_int(0, 60);

        clear_screen_char();
        char *number = (char *)malloc(6); // allocating 6 bytes for corresponding string
        sprintf(number, "%d", c);         // converting number to string
        while (*number)
        {

            write_char(x, y, *number);
            x++;
            number++;
            printf("hi\n");
        }
        a = b;
        b = c;

        for (int j = 0; j < 1000000000; j++)
            ; // busy wait for 1 sec nearly
    }
}