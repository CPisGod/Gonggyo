#include <stdio.h>
// 솔직히 내가 볼땐 이 코드는 효율성이 없음

int main() {
	int len, i, j;
	scanf("%d", &len);
	for (i = 1;i <= len;i++) {
		for (j = 1;j <= len;j++) {
			int n = i;
			if (j < n) {
				n = j;
			}
			if (len - i + 1 < n) {

				n = len - i + 1;
			}
			if (len - j + 1 < n) {
				n = len - j + 1;
			}
			if (n % 2 == 1) {
				printf("*");
			}
			else {
				printf(" ");
			}
		}
		printf("\n");
  }
}
