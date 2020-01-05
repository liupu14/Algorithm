public class fac{

	static long fac(int n){
		long result = 1;
		while(n>1){
			result *= n;
			n--;
		}
		return result;
	}

	public static void main(String[] args){
		System.out.print("10的阶乘是:");
		System.out.print(fac(10));
	}
}
