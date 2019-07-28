#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h> 
#include<pthread.h>
int sockfd = 0, n = 0;
pthread_t read_t,write_t;
char recvBuff[1024],s1[10000];int temp;
struct sockaddr_in serv_addr; 
char s[1000];
void *write_thread(void *argc)
{
	int sockfd=*(int*)argc;
	scanf(" %[^\t\n]s",s);
	if(!strcmp("exit",s))
	{
		write(sockfd, s, 1000);
		printf("\t\tclient says:Bye Bye\n");
		exit(0);
	}
	write(sockfd, s, 1000);
	return NULL;
}
void *read_thread(void *argc)
{
	int sockfd=*(int*)argc;	
	read(sockfd, s1, 1000);
	if(!strcmp(s1,"exit"))
	{
		printf("okay server TATA...\n");
		exit(0);
	}
	printf("\t\tserver said: %s\n", s1);
	return NULL;
}
int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("\n Usage: %s <ip of server> \n",argv[0]);
        return 1;
    } 
	
    memset(recvBuff, '0',sizeof(recvBuff));
    if((sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Error : Could not create socket \n");
        return 1;
    } 
	
    memset(&serv_addr, '0', sizeof(serv_addr)); 
	
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5000); 
    
    printf("Server address used is: %s\n", argv[1]);

    if(inet_pton(AF_INET, argv[1], &serv_addr.sin_addr)<=0)
    {
        printf("\n inet_pton error occured\n");
        return 1;
    } 
	char ch;
    	if( connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    	{
		printf("\n Error : Connect Failed \n");
		return 1;
    	} 
	printf("To exit any time write exit\n");
	while(true)
	{
		fflush(stdin);
		printf("client please write something\n");
		pthread_create(&write_t,NULL,write_thread,(void*)&sockfd);
		pthread_join(write_t,NULL);
		printf("waiting for server to write\n");
		pthread_create(&read_t,NULL,read_thread,(void*)&sockfd);
		pthread_join(read_t,NULL);
		fflush(stdin);
	}
    return 0;
}



