#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - creates 5 zombie processes.
 *
 * Return: void
 */

int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{

			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}

	while (1)
	{
		sleep(1);
	}
	return (0);
}
