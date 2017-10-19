package music;

import javax.sound.midi.MidiEvent;
import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequence;
import javax.sound.midi.Sequencer;
import javax.sound.midi.ShortMessage;
import javax.sound.midi.Track;

public class MusicTest1 {
	public static void main(String[] args){
		if(args.length < 2){
			System.out.println("args not satisfied");
		}else{
			int instrument = Integer.parseInt(args[0]);
			int note = Integer.parseInt(args[1]);
			System.out.println(instrument);
			System.out.println(note);
		}
		try{
			Sequencer player = MidiSystem.getSequencer();
			player.open();
			
			Sequence seq = new Sequence(Sequence.PPQ, 4);
			Track track = seq.createTrack();
			
			ShortMessage start = new ShortMessage();
			start.setMessage(192, 1, 44, 0);
			MidiEvent changeInstrument = new MidiEvent(start, 1);
			track.add(changeInstrument);
			
			ShortMessage a = new ShortMessage();
			a.setMessage(144, 1, 44, 100);
			MidiEvent noteOn = new MidiEvent(a, 1);
			track.add(noteOn);
			
			ShortMessage b = new ShortMessage();
			b.setMessage(128, 1, 44, 100);
			MidiEvent noteOff = new MidiEvent(b, 16);
			track.add(noteOff);
			
			player.setSequence(seq);
			player.start();
			System.out.println("success");
			
		}catch(Exception ex){
			System.out.println("error");
		}
		
	}
}
