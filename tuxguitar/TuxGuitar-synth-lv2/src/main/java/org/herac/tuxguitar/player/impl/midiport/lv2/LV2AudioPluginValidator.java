package org.herac.tuxguitar.player.impl.midiport.lv2;

import org.herac.tuxguitar.player.impl.midiport.lv2.jni.LV2Plugin;

public class LV2AudioPluginValidator implements LV2PluginValidator {

	@Override
	public boolean validate(LV2Plugin plugin) {
		if( plugin == null ) {
			return false;
		}
		if( plugin.getName() == null ) {
			System.err.println("Name not found: " + plugin.getUri());
			return false;
		}
		return (plugin.getAudioInputPortCount() > 0);
	}
}
