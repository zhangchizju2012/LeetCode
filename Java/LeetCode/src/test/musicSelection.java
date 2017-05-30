package test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

class Song implements Comparable<Song>{
	String name;
	Integer year;
	String singer;
	public Song(String n, int y, String s){
		name = n;
		year = y;
		singer = s;
	}
	public String getName(){
		return name;
	}
	public String toString(){// to make it printable.
		return name+':'+year+':'+singer;
	}
	@Override
	public int compareTo(Song o) { // to make it can be sorted by Collections.sort
		return name.compareTo(o.name);
	}
}

// //this one also works, can be seen in github history
//class Comparison {
//	public static Comparator<Song> name = new Comparator<Song>(){
//		@Override
//		public int compare(Song s1, Song s2){
//			return s1.name.compareTo(s2.name);
//		}
//	};
//	public static Comparator<Song> year = new Comparator<Song>(){
//		@Override
//		public int compare(Song s1, Song s2){
//			return s1.year.compareTo(s2.year);
//		}
//	};
//}


// 可以变成内部类：内部类最大的优点就在于它能够非常好的解决多重继承的问题（可能想继承多个抽象类或具体类而不仅是接口）
class ComparisonByYear implements Comparator<Song>{

	@Override
	public int compare(Song o1, Song o2) {
		// TODO Auto-generated method stub
		return o1.year.compareTo(o2.year);
	}
	
}

public class musicSelection {
	ArrayList<Song> songList = new ArrayList<>();
	ArrayList<String> nameList = new ArrayList<>();
	public static void main(String[] args){
		musicSelection ms = new musicSelection();
		ms.getSongList();
		System.out.println(ms.songList);
		//Collections.sort(ms.nameList);
		Collections.sort(ms.songList);
		System.out.println(ms.songList);
		//Collections.sort(ms.songList, Comparison.year);
		ComparisonByYear cby = new ComparisonByYear();
		Collections.sort(ms.songList, cby);
		System.out.println(ms.songList);
	}
	public void getSongList(){
		Scanner scanner;
		boolean label = true;
		while(label){
			System.out.println("Enter name, year and singer;");
			
			System.out.println("Enter name: ");
			scanner = new Scanner(System.in);
			String n = scanner.nextLine();
			System.out.println("Enter year: ");
			scanner = new Scanner(System.in);
			Integer y = scanner.nextInt();
			System.out.println("Enter singer: ");
			scanner = new Scanner(System.in);
			String s = scanner.nextLine();
			
			Song m = new Song(n, y, s);
			songList.add(m);
			nameList.add(n);
			System.out.println("Enter N to stop adding more songs, or enter any other things.");
			scanner = new Scanner(System.in);
			String temp = scanner.nextLine();
			if(temp.equals("N")){// doesn't work if use temp == "N", don't know why.
				label = false;
			}
		}
		
	}
}
