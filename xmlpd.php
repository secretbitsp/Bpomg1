<?

// +===========================================================================================+
// |                         Használtautó.hu HEX példa modul (c) 2011                          |
// +-------------------------------------------------------------------------------------------+
// |                                       Beállítások                                         |
// +-------------------------------------------------------------------------------------------+
// | Mennyi hirdetés jelenjen meg egy oldalon?                                                 |
$_hex['results_per_page'] = 10;
// +-------------------------------------------------------------------------------------------+
// | Weboldal címsora                                                                          |
$_hex['title'] = "Bemutató modul";
// +-------------------------------------------------------------------------------------------+
// | a "" kozé, a minta szó helyett írja be az export azonosítóját, amelyet emailben kapott!   |
$_hex['export_name'] = "minta";
// +-------------------------------------------------------------------------------------------+
// | A használni kívánt HEX verziószáma                                                        |
// | (újabbra áttéres esetén programfrissítés lehet szükséges)                                 |
$_hex['xml_version'] = "1.0";
// +-------------------------------------------------------------------------------------------+
// |                                  Gyorsítótár beállításai                                  |
// +-------------------------------------------------------------------------------------------+
// | Helyi cache állomány elérési útja                                                         |
$_hex['local_cache_file'] = 'cache/hasznaltauto_cache.temp';
// +-------------------------------------------------------------------------------------------+
// | Gyorsítótár elévülési ideje percekben megadva                                             |
$_hex['local_cache_minutes'] = 10;
// +-------------------------------------------------------------------------------------------+
// | Gyorsítótár letiltása - NEM AJÁNLOTT
$_hex['disable_local_cache'] = false;
// +-------------------------------------------------------------------------------------------+
// |                    Innentől kezdve kérem, NE szerkessze a fájlokat!                       |
// +===========================================================================================+

ini_set('memory_limit', '32M');
define('HEX_CLIENT_VERSION', '1.0');

/* Hibaüzenet kiírása START */
function errormessage($error) {
	echo "
	<p class=\"nincs_hird\">$error</p>";
	exit;
}
/* Hibaüzenet kiírása END */

/* CURL START */
function copen($url) {
	$curl = @curl_init();
	@curl_setopt($curl, CURLOPT_URL, $url);
	@curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	if (!$retval = @curl_exec($curl)) {	
		errormessage(@curl_error($curl));
	}
	@curl_close($curl);
	return $retval;
}
/* CURL END */

header('Content-Type: text/html; charset=utf-8');

echo "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML+RDFa 1.0//EN\" \"http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd\">
<html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"hu\">

<head>
	<title>{$_hex['title']}</title>
	<style type=\"text/css\">
		h2 {
			font-family: Verdana, sans-serif;
			font-size: 14pt;
		}
		a {
			color: #105FAE;
		}
		a:hover {
			color: #003E7D;
		}
		img {
			border: none;
		}
		table {
			border: none;
			border-collapse: collapse;
			border-spacing: 0;
		}
		table.lista {
			width: 650px;
		}
		table.adatlap {
			width: 400px;
			float: left;
		}
		img.kiskep {
			width: 79px;
			height: 59px;
		}
		div.kepek {
			float: left;
			width: 270px;
		}
		div.kepek img {
			margin: 0 0 5px 10px;
		}
		td, th, .nincs_hird, p {
			font-family: Verdana, sans-serif;
			font-size: 8pt;
			color: black;
			padding: 5px;
			text-align: left;
		}
		.tr_alt td {
			background-color: #f0f0f0;
		}
		.td a {
			color: black;
		}
		table.lista tr:hover td {
			background-color: #D3E6FA;
		}
		table.lista tr:hover td a, table.lista tr:hover td a:hover {
			color: #105FAE;
		}
		.nincs_hird {
			padding: 10px;
			text-align: center;
			font-weight: bold;
		}
	</style>
</head>

<body>";


/* Kliens oldali gyorsítótárazás START */

if ($_hex['disable_local_cache'] || !is_file($_hex['local_cache_file']) || filemtime($_hex['local_cache_file']) < time() - 60 * $_hex['local_cache_minutes']) {
	
	/* HEX XML és HEX XSD állományok letöltése START */
	
	$xml_url = "http://hex.hasznaltauto.hu/{$_hex['xml_version']}/xml/{$_hex['export_name']}";
	$xsd_url = "http://hex.hasznaltauto.hu/{$_hex['xml_version']}/hex.xsd";
	
	if (ini_get("allow_url_fopen")) {
		$xml_string = @file_get_contents($xml_url);
		$xsd_string = @file_get_contents($xsd_url);
	} else if (function_exists("curl_init")) {
		$xml_string = copen($xml_url);
		$xsd_string = copen($xsd_url);
	} else {
		errormessage("A HEX állományok nem tölthetőek le, mert a szerver beállításai ezt nem teszik lehetővé.");
	}
	
	if (!$xml_string || !$xsd_string) {
		errormessage("Hiba a HEX állományok letöltése közben.");
	}
	/* HEX XML és HEX XSD állományok letöltése END */
	
	
	/* HEX XML ellenőrzése START */
	
	libxml_use_internal_errors(true);
	$objDomDocument = new DomDocument();
	$objDomDocument->loadXML($xml_string);
	
	if (!$hirdetesek = @simplexml_import_dom($objDomDocument)) {
		errormessage("A feldolgozandó XML üres, vagy nem XML adatokat tartalmaz: $xml_url");
	}
	
	if ($hirdetesek->getName() != 'hirdetesek') {
		errormessage("HEX hiba: " . (string)$hirdetesek);
	}
		
	if (!isset($hirdetesek->attributes()->min_client_version) || !isset($hirdetesek->attributes()->max_client_version)) {
		errormessage("A használt XML nem tartalmazza a szükséges kliens-verziószám megkötéseket. Az XML nem dolgozható fel.");
	}
	
	if (version_compare(HEX_CLIENT_VERSION, (string)$hirdetesek->attributes()->min_client_version) < 0 || version_compare((string)$hirdetesek->attributes()->max_client_version, HEX_CLIENT_VERSION) < 0) {
		errormessage("A használni kívánt HEX XML nem használható ezzel a programmal. Kérem, ellenőrizze a verziószámokat és szükség esetén frissítse a HEX klienst!");
	}
	
	if (!@$objDomDocument->schemaValidateSource($xsd_string)) {
		$xsd_errors = array();
		foreach (libxml_get_errors() as $eachError) {
			$xsd_errors[] = $eachError->message;
		}
		errormessage("Az XML nem felel meg a sémának. Hibák: " . implode("/n", $xsd_errors));
	}
	
	$hirdetesek_szama = count($hirdetesek->children());
	if ($hirdetesek_szama == 0) {
		errormessage("Jelenleg nincsenek megjeleníthető hirdetések.");
	}
	
	/* HEX XML ellenőrzése END */
	
	
	/* HEX XML adatainak feldolgozása tömbbe START */
	
	$adatok = array();
	$i = 0;
	
	foreach ($hirdetesek->children() as $hirdetes) {
		
		$adatok[$i] = array(
			'hirdeteskod'	=> (int)$hirdetes->attributes()->hirdeteskod,
			'gyartmany'	=> (string)$hirdetes->attributes()->gyartmany,
			'tipus'		=> (string)$hirdetes->attributes()->tipus,
			'kategoria'	=> (string)$hirdetes->attributes()->kategoria,
			'adatok'	=> array(),
			'kepek'		=> array()
		);
		
		foreach ($hirdetes->children() as $elem) {
			if ($elem->getName() == 'kepek') {
				foreach($elem->children() as $kep) {
					$adatok[$i]['kepek'][] = array(
						'kicsi' => (string)$kep->attributes()->kicsi,
						'kozepes' => (string)$kep->attributes()->kozepes,
						'nagy' => (string)$kep
					);
				}
			} else {
				$adatok[$i]['adatok'][(string)$elem->getName()] = array(
					'nev'	=> (string)$elem->attributes()->megnevezes,
					'ertek'	=> (string)$elem
				);
			}
		}
		
		$i++;
	}
	
	/* HEX XML adatainak feldolgozása tömbbe END */

	
	/* Helyi gyorsítótár-állomány írása START */
	
	if (!$_hex['disable_local_cache'] && (!is_file($_hex['local_cache_file']) || is_writable($_hex['local_cache_file']))) {
		$handle = fopen($_hex['local_cache_file'], "w");
		fwrite($handle, serialize($adatok));
		fclose($handle);
	}
	
	/* Helyi gyorsítótár-állomány írása START */
	
} else if (is_file($_hex['local_cache_file'])) {

	/* Helyi gyorsítótár-állomány beolvasása START */

	$adatok = unserialize(file_get_contents($_hex['local_cache_file']));
	$hirdetesek_szama = count($adatok);
	
	/* Helyi gyorsítótár-állomány beolvasása END */
}
/* Kliens oldali gyorsítótárazás END */

if (isset($_GET['hirdeteskod']) && is_numeric($_GET['hirdeteskod'])) {

	$row = false;
	foreach ($adatok as $sorszam => $tartalom) {
		if ($tartalom['hirdeteskod'] == $_GET['hirdeteskod']) {
			$row = $tartalom;
		}
	}
	
	if (!$row) {
		errormessage("A megadott kódú hirdetés nem található az adatbázisban!");
	} else {
		
		
		if (isset($_GET['kep']) && is_numeric($_GET['kep'])) {
			
			/* KÉP megjelenítése START */
			
			foreach ($row['kepek'] as $kepindex => $kep) {
				if ($kepindex == $_GET['kep']) {
					$nagykep = $kep;
					break;
				}
			}
			if (isset($nagykep)) {
				echo "
		<div style=\"text-align: center; width: 640px; height: 480px; margin: auto\">
			<a href=\"javascript:window.self.close();\"><img src=\"{$kep['nagy']}\" /></a>
		</div>";
			} else {
				errormessage("A megadott kép nem található az adatbázisban!");
			}
			
			/* KÉP megjelenítése END */
			
		} else {
			
			/* Jármű adatlapja START */
			
			echo "
		<h2>{$row['gyartmany']} {$row['tipus']}</h2>
		<table class=\"adatlap\">";
			$i = 0;
			foreach ($row['adatok'] as $elem) {
				echo "
			<tr" . ($i % 2 == 0 ? " class=\"tr_alt\"" : "") . ">
				<td>{$elem['nev']}:</td>
				<td>{$elem['ertek']}</td>
			</tr>";
				$i++;
			}
			
			echo "
		</table>
		<div class=\"kepek\">";
			foreach ($row['kepek'] as $kepindex => $kep) {
				echo "<a href=\"?hirdeteskod={$_GET['hirdeteskod']}&kep={$kepindex}\" onclick=\"window.open('?hirdeteskod={$_GET['hirdeteskod']}&kep={$kepindex}', 'image', 'width=660,height=500'); return false;\" title=\"\"><img src=\"{$kep['kozepes']}\" alt=\"\" /></a>";
			}	
			echo "
		</div>
		<p style=\"text-align: center; clear: both; width: 670px;\"><a href=\"javascript:history.go(-1);\">&laquo; Vissza</a></p>";
		
			/* Jármű adatlapja END */
		}
	}
	

} else {

	/* Hirdetések listázása START */
	
	$page  = isset($_GET['page']) && is_numeric($_GET['page']) && ($_GET['page'] - 1) * $_hex['results_per_page'] < $hirdetesek_szama ? $_GET['page'] : 1;
	
	$from = ($page - 1) * $_hex['results_per_page'];
	$to = min($page * $_hex['results_per_page'] - 1, $hirdetesek_szama - 1);
	
	echo "
	<h2>Adatbázisban talált járművek</h2>
	<table class=\"lista\">
		<tr>
			<td colspan=\"7\" style=\"font-weight: bold; height: 40px; text-align: right;\">Találatok száma: " . count($adatok) . "</td>
		</tr>
		<tr>
			<th></th>
			<th></th>
			<th>Gyártmány, típus</th>
			<th style=\"text-align: center;\">Vételár</th>
			<th>Évjárat</th>
			<th style=\"text-align: center;\">Telj.</th>
			<th style=\"text-align: center;\">Motor</th>
		</tr>";

	for ($i = $from; $i <= $to; $i++) {
		echo "
		<tr" . ($i % 2 == 0 ? " class=\"tr_alt\"" : "") . ">
			<td style=\"height: 45px; width: 20px;\">" . ($i+1) . ".</td>
			<td style=\"width: 65px;\">" . (count($adatok[$i]['kepek']) > 0 ? "<a href=\"?hirdeteskod={$adatok[$i]['hirdeteskod']}\"><img src=\"{$adatok[$i]['kepek'][0]['kicsi']}\" alt=\"\" class=\"kiskep\"/></a>" : "&nbsp;") . "</td>
			<td style=\"width: 280px;\"><a href=\"?hirdeteskod={$adatok[$i]['hirdeteskod']}\">{$adatok[$i]['gyartmany']} {$adatok[$i]['tipus']}</a></td>
			<td style=\"width: 400px; text-align: center;\">{$adatok[$i]['adatok']['ar']['ertek']}</td>
			<td style=\"text-align: center;\">{$adatok[$i]['adatok']['evjarat']['ertek']}</td>
			<td style=\"width: 130px; text-align: center;\">" . (isset($adatok[$i]['adatok']['teljesitmeny']) ? $adatok[$i]['adatok']['teljesitmeny']['ertek'] : "&nbsp;") . "</td>
			<td style=\"width: 200px; text-align: center;\">" . (isset($adatok[$i]['adatok']['uzemanyag']) ? $adatok[$i]['adatok']['uzemanyag']['ertek'] : "&nbsp;")."</td>
		</tr>";
	}
	echo "
	</table>";

	/* Oldalszámozás START */
	if ($to < $hirdetesek_szama - 1 || $from > 0) {
		echo "
	<p style=\"width: 640px; text-align: right;\">" .
	($from > 0 ? "<a href=\"?page=" . ($page - 1) . "\" title=\"Előző oldal\">&laquo; Előző</a>" :"") .
	($to < $hirdetesek_szama - 1 && $from > 0 ? " | " : "") . 
	($to < $hirdetesek_szama - 1 ? "<a href=\"?page=" . ($page + 1) . "\" title=\"Következő oldal\">Következő &raquo;</a>" : "") . "
	</p>";	
	}
	/* Oldalszámozás END */
	
	/* Hirdetések listázása START */
}
/* Oldalak megjelenítése START */

echo "
</body>

</html>";


?>
