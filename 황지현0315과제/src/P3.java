import java.util.Scanner;

public class P3 {
	public static void ModifyArray(int intArray[]) {
		for(int i=0;i<intArray.length;i++) {
			if(intArray[i]>=10) {
				intArray[i]=0;
			}
		}
	}

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int length=input.nextInt();
		int intArray[]=new int[length];
		for(int i=0;i<length;i++) {
			intArray[i]=input.nextInt();
		}
		ModifyArray(intArray);
		for(int i=0;i<intArray.length;i++) {
			System.out.println(intArray[i]);
		}
	}

}