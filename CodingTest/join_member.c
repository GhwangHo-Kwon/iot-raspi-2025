#include "join_member.h"

void Menu()
{
    int num;

    FILE *file = fopen("userFile.txt", "a");
    if (file == NULL) {
        printf("파일 열기 실패!\n");
        return;
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
}

void joinMember()
{
    char *id, *pw, *confirmPw;

    id = (char *)malloc(100 * sizeof(char));
    pw = (char *)malloc(100 * sizeof(char));
    confirmPw = (char *)malloc(100 * sizeof(char));

    if (id == NULL || pw == NULL || confirmPw == NULL) {
        printf("메모리 할당 실패!\n");
        return;
    }

    printf("회원가입\n");

    while (1) {
        printf("ID: ");
        fgets(id, 100, stdin);
        id[strcspn(id, "\n")] = '\0';

        if (idSearch(id) == 1) {
            printf("이미 존재하는 ID입니다.\n다시 입력해 주세요!\n");
            getchar();
            system("clear");
        }
        else {
            break;
        }
    }

    while (1) {
        printf("PW: ");
        fgets(pw, 100, stdin);
        pw[strcspn(pw, "\n")] = '\0';

        if (strlen(pw) < 5) {
            system("clear");
            printf("비밀번호는 5자 이상이어야 합니다.\n다시 입력해 주세요!\n");
            continue;
        }

        printf("비밀번호 확인: ");
        fgets(confirmPw, 100, stdin);
        confirmPw[strcspn(confirmPw, "\n")] = '\0';

        if (strcmp(pw, confirmPw) != 0) {
            system("clear");
            printf("비밀번호가 일치하지 않습니다.\n다시 입력해 주세요!\n");
        }
        else {
            break;
        }
    }

    userFile(id, pw);

    free(id);
    free(pw);
    free(confirmPw);
}

int idSearch(char *id)
{
    char line[256];
    int found = 0;
    char file_id[100];

    FILE *file = fopen("userFile.txt", "r");
    
    if (file == NULL) {
        printf("파일 열기 실패!\n");
        return -1;
    }

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';
        char *token = strtok(line, ",");

        if (token != NULL) {
            strcpy(file_id, token);
            if (strcmp(id, file_id) == 0) {
                found = 1;
                break;
            }
        }
    }
    fclose(file);

    return found;
}

void userFile(char *id, char *pw)
{
    FILE *file = fopen("userFile.txt", "a");
    if (file == NULL) {
        printf("파일 열기 실패!\n");
        return;
    }

    fprintf(file, "%s,%s\n", id, pw);
    fclose(file);
    
    system("clear");

    printf("회원가입 성공\n");
    printf("ID: %s, PW: %s\n", id, pw);
}

void userLogin()
{
    char line[256];
    int found = 0;
    char file_id[100], file_pw[100];
    char *id, *pw;
    id = (char *)malloc(100 * sizeof(char));
    pw = (char *)malloc(100 * sizeof(char));

    FILE *file = fopen("userFile.txt", "r");
    if (file == NULL) {
        printf("파일 열기 실패!\n");
        return;
    }

    if (id == NULL || pw == NULL) {
        printf("메모리 할당 실패!\n");
        return;
    }

    printf("로그인\n");

    printf("ID: ");
    fgets(id, 100, stdin);
    id[strcspn(id, "\n")] = '\0';
    
    printf("PW: ");
    fgets(pw, 100, stdin);
    pw[strcspn(pw, "\n")] = '\0';

    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = '\0';

        char *token = strtok(line, ",");
        if (token != NULL) {
            strcpy(file_id, token);
            token = strtok(NULL, ",");
            if (token != NULL) {
                strcpy(file_pw, token);
                if (strcmp(id, file_id) == 0 && strcmp(pw, file_pw) == 0) {
                    found = 1;
                    break;
                }
            }
        }
    }
    
    system("clear");

    if (found == 1) {
        printf("로그인 성공!\n");
        printf("ID: %s, PW: %s\n", id, pw);
    }
    else {
        printf("로그인 실패!\nID 또는 PW가 잘못되었습니다.\n");
    }
    fclose(file);
    free(id);
    free(pw);
}