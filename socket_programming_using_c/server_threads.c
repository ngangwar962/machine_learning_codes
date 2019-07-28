#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <time.h> 
#include<pthread.h>
int listenfd = 0, connfd = 0;
pthread_t server_rthread,server_wthread;
struct sockaddr_in serv_addr; 
char s[10000],s1[10000];
char sendBuff[1025];
int temp;
void *server_read(void *argc)
{
	int connfd1=*(int*)argc;
	printf("waiting for client to write\n");
	read(connfd1,s,1000);
	if(!strcmp(s,"exit"))
	{
		printf("\t\tserver says:okay Bye Bye\n");
		exit(0);
	}
	printf("\tclient said: %s\n",s);
	return NULL;
}
void *server_write(void *argc)
{
	int connfd1=*(int*)argc;
	scanf(" %[^\t\n]s",s1);
	if(!strcmp(s1,"exit"))
	{
		write(connfd, s1, 1000);
		printf("\t\tserver says:I am going TATA.....\n");
		exit(0);
	}
	write(connfd1, s1, 1000);
	fflush(stdin);
	return NULL;

}
int main(int argc, char *argv[])
{
    time_t ticks; 
	
    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, '0', sizeof(serv_addr));
    memset(sendBuff, '0', sizeof(sendBuff)); 
	
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(5000); 
	
    bind(listenfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)); 
	
    if(listen(listenfd, 50)==0)
    printf("Listening\n");
    else
    printf("Error\n");
    pthread_t tid[60]; 
    char ch;
    connfd = accept(listenfd, (struct sockaddr*)NULL, NULL);
    while(1)
    {
	fflush(stdin);
	addr_size = sizeof serverStorage;
	newSocket = accept(serverSocket, (struct sockaddr *) &serverStorage, &addr_size);
	//for each client request creates a thread and assign the client request to it to process
	//so the main thread can entertain next request
	/*if( pthread_create(&tid[i], NULL, socketThread, &newSocket) != 0 )
	printf("Failed to create thread\n");*/
	if( i >= 50)
	{
	  i = 0;
	  while(i < 50)
	  {
	    pthread_join(tid[i++],NULL);
	  }
	  i = 0;
        }
	pthread_create(&tid[i],NULL,server_read,(void*)&connfd);
	pthread_join(server_rthread,NULL);
	printf("server is writing\n");
	pthread_create(&server_wthread,NULL,server_write,(void*)&connfd);
	pthread_join(server_wthread,NULL);
    }
    close(connfd);
return 0;
}
