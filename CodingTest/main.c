#include "join_member.h"

int main()
{
    int num;

    FILE *file = fopen("userFile.txt", "a");
    if (file == NULL) {
        printf("파일 열기 실패!\n");
        return -1;
    }
    fclose(file);
    
    while (1) {
        system("clear");
        printf("회원가입, 로그인 프로그램\n");
        printf("1. 회원가입\n2. 로그인\n3. 종료\n");
        scanf("%d", &num);
        getchar();

        if (num == 1) {
            system("clear");
            joinMember();
            getchar();
        }
        else if (num == 2) {
            system("clear");
            userLogin();
            getchar();
        }
        else if (num == 3) {
            system("clear");
            printf("프로그램 종료\n");
            break;
        }
        else {
            system("clear");
            printf("번호를 다시 입력해 주세요!\n");
            getchar();
        }
        num = 0;
    }

    return 0;
}


