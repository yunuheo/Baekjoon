import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        int[] cli = new int[N];

        for (int i = 0; i < N; i++) {
            cli[i] = sc.nextInt();
        }

        Arrays.sort(cli); //cli 배열 오름차순 정렬
        int sum = 0;


        for (int i = 1; i <= cli.length; i++) {
            for (int j = 0; j < i; j++) {
                sum = sum + cli[j];
            }
        }
        System.out.println(sum);

    }
}