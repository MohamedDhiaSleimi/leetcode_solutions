// WARNING: CHANGE HERE for return type and comparison logic
bool testing(int res, int expected) { 
    return res == expected;
}

int main() {
    struct TestCase {
        char* input;//WARNING: CHANGE HERE for the input type
        int expected; //WARNING: CHANGE HERE for the expected result type
    };

    struct TestCase test_cases[] = { // WARNING: CHANGE HERE for your actual test cases
    };

    int num_test_cases = sizeof(test_cases) / sizeof(test_cases[0]);

    char **warn_list = malloc(num_test_cases * sizeof(char*));
    int warn_count = 0;

    for (int i = 0; i < num_test_cases; i++) {
        int res = your_function(test_cases[i].input); // WARNING: CHANGE HERE for your function call and result type
        if (!testing(res, test_cases[i].expected)) {
            warn_list[warn_count] = malloc(100 * sizeof(char));
            snprintf(warn_list[warn_count], 100, "Input: %s, Expected: %d, Got: %d", // WARNING: CHANGE HERE for the type format specifier
                     test_cases[i].input,
                     test_cases[i].expected,
                     res);
            warn_count++;
        } else {
            printf("_________________________________\n");
            printf("Input: %s, Result: %d\n", // WARNING: CHANGE HERE for the type format specifier
                   test_cases[i].input,
                   res);
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

