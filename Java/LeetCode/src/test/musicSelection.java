package test;

import java.util.ArrayList;
import java.util.Scanner;

class Song {
	String name;
	int year;
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
		return name;
	}
}

public class musicSelection {
	ArrayList<Song> songList = new ArrayList<>();
	public static void main(String[] args){
		musicSelection ms = new musicSelection();
		ms.getSongList();
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
			int y = scanner.nextInt();
			System.out.println("Enter singer: ");
			scanner = new Scanner(System.in);
			String s = scanner.nextLine();
			
			Song m = new Song(n, y, s);
			songList.add(m);
			System.out.println("Enter N to stop adding more songs, or enter any other things.");
			scanner = new Scanner(System.in);
			String temp = scanner.nextLine();
			if(temp.equals("N")){// doesn't work if use temp == "N", don't know why.
				label = false;
			}
		}
		
	}
}
