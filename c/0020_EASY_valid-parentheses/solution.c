
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

bool isValid(char *s) {
    int len = strlen(s);
    char stack[len];
    int top = -1;

    for (int i = 0; i < len; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stack[++top] = s[i];
        } else {
            if (top == -1)
                return false;
            if (s[i] == ')' && stack[top] != '(')
                return false;
            if (s[i] == '}' && stack[top] != '{')
                return false;
            if (s[i] == ']' && stack[top] != '[')
                return false;
            top--;
        }
    }
    return top == -1;
}

bool testing(bool res, bool expected) {
    return res == expected;
}

int main() {
    struct TestCase {
        char* input;
        bool expected;
    };

    struct TestCase test_cases[] = {
        {"()", true},
        {"()[]{}", true},
        {"(]", false},
        {"{[]}", true},
        {"([)]", false}
    };

    int num_test_cases = sizeof(test_cases) / sizeof(test_cases[0]);

    char **warn_list = malloc(num_test_cases * sizeof(char*));
    int warn_count = 0;

    for (int i = 0; i < num_test_cases; i++) {
        bool res = isValid(test_cases[i].input);
        if (!testing(res, test_cases[i].expected)) {
            warn_list[warn_count] = malloc(100 * sizeof(char));
            snprintf(warn_list[warn_count], 100, "Input: %s, Expected: %s, Got: %s",
                     test_cases[i].input,
                     test_cases[i].expected ? "true" : "false",
                     res ? "true" : "false");
            warn_count++;
        } else {
            printf("_________________________________\n");
            printf("Input: %s, Result: %s\n",
                   test_cases[i].input,
                   res ? "true" : "false");
        }
    }

    printf("=================================\n");
    if (warn_count > 0) {
        printf("errors!!\n");
        for (int i = 0; i < warn_count; i++) {
            printf("%s\n", warn_list[i]);
            free(warn_list[i]); 
        }
        printf("_________________________________\n");
    }

    free(warn_list); 

    return 0;
}

