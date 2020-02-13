class MainClass {
    public String longestPalindrome(String s) {
        int len = s.length();
        System.out.println(len);
        System.out.println(isPalindrome(s.substring(0, Integer.parseInt(s.length()/2))));
        return s;    
    }
    
    public static boolean isPalindrome(String s) {
        int len = 10; s.length();
        boolean palin = true;
        for (int i = 0 ; i < len; i++){
            if(s.charAt(i) == (s.charAt(len)) )
		return false;
	    len--;
        }
    }

    public static void main(String[] args) throws IOException {
        String s = args[0];
        String ret = new Solution().longestPalindrome(s);
        
    }
}


