import langid



def find_lang(string):

	print "\n\n\n\t\t\tReading from file"

	print "\n\n\n\t\t\tProcessing"

	result=langid.classify(string)



	languages= { 'af' : 'Afrikaans', 
				 'am' : 'Amharic',
				 'an' : 'Arangonese',
				 'ar' : 'Arabic', 
				 'as' : 'Assamese',
				 'az' : 'Azerbaijani',
				 'be' : 'Belarusian',
			     'bg' : 'Bulgarian', 
			     'bn' : 'Bengali', 
			     'br' : 'Breton', 
			     'bs' : 'Bosnian',
			     'ca' : 'Catalan' ,
			     'cs' : 'Czech', 
			     'cy' : 'Welsh', 
			     'da' : 'Danish',
			     'de' : 'German', 
			     'dz' : 'Dzongkha', 
				 'el' : 'Greek', 
				 'en' : 'English', 
				 'eo' : 'Esperanto',
				 'es' : 'Spanish', 
				 'et' : 'Estonian',
				 'eu' : 'Basque',
				 'fa' : 'Persian',
				 'fi' : 'Finnish',
				 'fo' : 'Faroese'
			   }


 	print "\n\n\n\t\t\tLanguage is detected as {}".format(languages[result[0]])

 	return






#fr, ga, gl, gu, he, hi, hr, ht, hu, hy, id, is, it, ja, jv, ka, kk, km, kn, ko, ku, ky, la, lb, lo, lt, lv, mg, mk, ml, mn, mr, ms, mt, nb, ne, nl, nn, no, oc, or, pa, pl, ps, pt, qu, ro, ru, rw, se, si, sk, sl, sq, sr, sv, sw, ta, te, th, tl, tr, ug, uk, ur, vi, vo, wa, xh, zh, zu}