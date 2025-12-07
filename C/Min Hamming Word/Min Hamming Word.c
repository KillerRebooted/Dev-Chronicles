#include <stdio.h>

int strlength(char str[]) {
    int count = 0;
    while (str[count]) {
        count++;
    }
    return count;
}

int next_space(char str[], int start) {
    for (int i = start; i < 100; i++) {
        if (str[i] == ' ') {
            return i;
        }
        else if (str[i] == '\0') {
            return 0;
        }
    }
}

void main(){
    char sentence[100];
    char query[100];

    printf("Enter a sentence: ");
    fgets(sentence, 100, stdin);

    printf("Enter a word to search: ");
    fgets(query, 100, stdin);

    sentence[strlength(sentence)-1] = '\0';
    query[strlength(query)-1] = '\0';

    char min_hamming_word[100];
    int min_hamming_distance = 100;

    int start = 0, end, hamming;
    for (int i = 0; i < 100; i++) {

        hamming = 0;
        end = next_space(sentence, start);
        if (!end) {
            break;
        }

        if (end-start != strlength(query)) {
            hamming += (end-start < strlength(query))?(strlength(query)-(end-start)):((end-start)-strlength(query));
        }

        for (int j = start; j < end; j++) {
            if (query[j-start] == '\0') {
                break;
            }
            else if (sentence[j] != query[j-start]) {
                hamming++;
            }
        }

        if (hamming < min_hamming_distance) {
            min_hamming_distance = hamming;
            for (int k = start; k < end; k++) {
                min_hamming_word[k-start] = sentence[k];
            }
        }

        start = end+1;

    }

    printf("\nThe word with minimum Hamming Distance to \"%s\" is: \"%s\" with Hamming Distance %d", query, min_hamming_word, min_hamming_distance);

}
