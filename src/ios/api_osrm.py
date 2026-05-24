import requests

OSRM_BASE = "https://router.project-osrm.org/route/v1/driving"

def buscar_rota_osrm(coordenadas: list[tuple[float, float]]) -> dict | None:
  
    pontos = ";".join(f"{lon},{lat}" for lat, lon in coordenadas) 
    url = f"{OSRM_BASE}/{pontos}"

    params = {
        "overview":   "full",
        "geometries": "geojson",
        "steps":      "true",
    }

    try: 
        resposta = requests.get(url, params=params, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        if dados.get("code") != "Ok" or not dados.get("routes"):
            return None

        rota = dados["routes"][0]
        rodovias = []
        for leg in rota.get("legs", []):
            for step in leg.get("steps", []):
                nome = step.get("name", "").strip()

                if nome and any(uf in nome.upper() for uf in [
                    "BR-","SP-","MG-","RJ-","PR-","RS-","SC-","BA-",
                    "GO-","DF-","ES-","MS-","MT-","PA-","CE-","PE-"
                ]):
                    if not rodovias or rodovias[-1] != nome:
                        rodovias.append(nome)

        geometria = [
            [ponto[1], ponto[0]]   
            for ponto in rota["geometry"]["coordinates"]
        ]

        return {
            "geometry":  geometria,
            "distancia": round(rota["distance"] / 1000, 1),
            "duracao":   round(rota["duration"] / 60, 1),
            "rodovias":  rodovias, 
        }

    except requests.exceptions.Timeout:
        print("[OSRM] Timeout na requisição")
        return None

    except requests.exceptions.RequestException as e:
        print(f"[OSRM] Erro na requisição: {e}")
        return None