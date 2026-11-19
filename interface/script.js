// Minhas classes, igual eu fiz no Python lá no app.py
// Copiei a mesma ideia do professor pra não dar conflito

class Motorista{
    constructor(n,p,t,f,car,nota){
        this.nome=n; // nome do cara
        this.placa=p; // placa do carro
        this.tipo_carro=t; // se é ECONOMY, COMFORT ou BLACK
        this.foto=f; // fotinha dele
        this.carro=car;
        this.nota=nota; // nota dele
        this.disponivel=true; // se tá livre ou não
        this.tempoRestante=0; // quanto tempo falta pra acabar a corrida
    }
}
class Passageiro{
    constructor(n,c){ this.nome=n; this.cpf=c; }
}
class Corrida{
    constructor(pas,mot,ori,des,dist){
        this.passageiro=pas; this.motorista=mot; this.origem=ori; this.destino=des; this.distancia=dist;
        this.valor=0; this.status="em andamento"; this.calcularPreco();
    }
    // Aqui é a conta que o professor passou, R$5 de bandeirada + km * preço do tipo
    calcularPreco(){
        let km=1.5; // preço base do ECONOMY
        if(this.motorista.tipo_carro=="COMFORT") km=2.2; // COMFORT é mais caro
        if(this.motorista.tipo_carro=="BLACK") km=3.5; // BLACK é o mais caro, de luxo
        this.valor=5+this.distancia*km;
    }
    // Tempo que o motorista vai ficar ocupado, quanto mais longe mais tempo
    tempoTotalSeg(){ return Math.ceil(this.distancia*2+15); }
}

// Lista de motoristas que já deixei pronto, com idade entre 30 e 45 que você pediu
let motoristas=[
 new Motorista("Fernanda 38a","BRA2E19","ECONOMY","https://i.pravatar.cc/150?img=26","Onix",4.9),
 new Motorista("Rafael 34a","ABC1D23","COMFORT","https://i.pravatar.cc/150?img=12","Corolla",5.0),
 new Motorista("Patricia 41a","SUL4R22","BLACK","https://i.pravatar.cc/150?img=32","Mercedes",4.8),
 new Motorista("Marcos 36a","JKL3M45","ECONOMY","https://i.pravatar.cc/150?img=15","HB20",4.7),
 new Motorista("Juliana 32a","XYZ9K88","COMFORT","https://i.pravatar.cc/150?img=5","Jeep",5.0),
 new Motorista("Roberto 44a","PON7A23","BLACK","https://i.pravatar.cc/150?img=8","Hilux",4.9)
];

let passageiros=[], corridas=[], corridasAtivas=[], motoristaSelecionado=null;
let map, markerTaxi, rotaLine, corridaAtual=null, animInterval=null;

// Coordenadas de algumas cidades, pra o mapa saber onde colocar o ponto
// Coloquei Rio Negrinho como base porque é de onde você é
const cidades={
 "rio negrinho":[-26.25,-49.52], "curitiba":[-25.43,-49.27], "são paulo":[-23.55,-46.63],
 "joinville":[-26.30,-48.84], "florianopolis":[-27.59,-48.54], "default":[-26.25,-49.52]
};
// Pega a coordenada, se não achar inventa uma perto
function getCoord(nome){
    nome=nome.toLowerCase();
    for(let k in cidades){ if(nome.includes(k)) return cidades[k]; }
    return [cidades.default[0]+(Math.random()-0.5)*2, cidades.default[1]+(Math.random()-0.5)*2];
}

// Função que troca de aba, esconde todas e mostra só a que clicou
function aba(n){
 document.querySelectorAll("main > section").forEach(s=>s.classList.add("hidden"));
 document.getElementById("aba-"+n).classList.remove("hidden");
 document.querySelectorAll(".tabs button").forEach(b=>b.classList.remove("ativo"));
 document.getElementById("t"+(n=="motoristas"?1:n=="passageiro"?2:n=="corrida"?3:n=="mapa"?4:5)).classList.add("ativo");
 if(n=="motoristas"||n=="corrida") renderMotoristas();
 if(n=="mapa") setTimeout(()=>{ if(map) map.invalidateSize(); else initMap(); },200);
 if(n=="historico") renderHist();
}

// Inicia o mapa, pega do OpenStreetMap que é de graça
function initMap(){
 map=L.map('map').setView([-26.25,-49.52],7);
 L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution:'© OpenStreetMap'}).addTo(map);
}

// Mostra os motoristas na tela
function renderMotoristas(){
 let html=""; 
 motoristas.forEach((m,i)=>{
   html+=`<div class="card motorista ${!m.disponivel?'ocupado':''} ${motoristaSelecionado==i?'selecionado':''}" onclick="selecionarMotorista(${i})"><img src="${m.foto}"><h3>${m.nome} ${!m.disponivel?'🔴':'🟢'}</h3><span class="tag ${m.tipo_carro}">${m.tipo_carro}</span><br><small>⭐ ${m.nota} • ${m.carro}</small>${!m.disponivel?`<br><b>⏱️ ${m.tempoRestante}s</b>`:`<br><small>Clique para escolher</small>`}</div>`
 }); 
 document.getElementById("lista-motoristas").innerHTML=html; 
 filtrarMotoristas();
}
function filtrarMotoristas(){
 let tipo=document.getElementById("c-tipo")?.value||"ECONOMY"; 
 let div=document.getElementById("motoristas-disponiveis"); if(!div) return;
 let lista=motoristas.map((m,i)=>({m,i})).filter(x=>x.m.tipo_carro==tipo&&x.m.disponivel);
 div.innerHTML=lista.length==0?`<p>Sem motorista ${tipo}</p>`:lista.map(x=>`<div class="card motorista ${motoristaSelecionado==x.i?'selecionado':''}" onclick="selecionarMotorista(${x.i})"><img src="${x.m.foto}" style="width:60px;height:60px"><br>${x.m.nome}</div>`).join(""); 
 calcPrev();
}

// Quando clica no motorista já vai pra parte de passageiro, como você pediu
function selecionarMotorista(i){
 if(!motoristas[i].disponivel) return; // se já tá em corrida não deixa
 motoristaSelecionado=i;
 renderMotoristas();
 calcPrev();
 aba("passageiro"); // joga direto pro cadastro de passageiro
 document.getElementById("p-nome").focus();
}

// Atualiza o preço na hora que muda a distância
function calcPrev(){
 let dist=parseFloat(document.getElementById("c-dist").value)||0; 
 let tipo=document.getElementById("c-tipo").value; 
 let km=tipo=="ECONOMY"?1.5:tipo=="COMFORT"?2.2:3.5; 
 let valor=5+dist*km;
 document.getElementById("valorBtn").textContent=valor.toFixed(2);
 document.getElementById("previa").innerHTML=`💰 R$ ${valor.toFixed(2)} • ⏱️ ${Math.ceil(dist*2+15)}s • ${dist}KM`;
 document.getElementById("kmLabel").textContent=dist;
}

// Cadastrar motorista e passageiro, bem simples
function addMotorista(){let n=document.getElementById("m-nome").value.trim(), p=document.getElementById("m-placa").value.trim().toUpperCase(), t=document.getElementById("m-tipo").value; if(n.length<3||!t)return alert("Preencha nome e tipo"); motoristas.push(new Motorista(n,p,t,`https://i.pravatar.cc/150?u=${n}`,"Novo",5.0)); renderMotoristas();}
function addPassageiro(){let n=document.getElementById("p-nome").value.trim(), c=document.getElementById("p-cpf").value.trim(); if(n.length<3||c.length!=11)return alert("CPF precisa ter 11 números"); passageiros.push(new Passageiro(n,c)); renderPassageiros(); alert("Passageiro cadastrado! Agora vai em Solicitar");}
function renderPassageiros(){document.getElementById("lista-passageiros").innerHTML=passageiros.map(p=>`<div class="card">🧑 ${p.nome} - ${p.cpf}</div>`).join("")}

// Solicita a corrida e começa a animação no mapa
function solicitar(){
 let cpf=document.getElementById("c-cpf").value.trim(), ori=document.getElementById("c-origem").value.trim(), des=document.getElementById("c-destino").value.trim(), dist=parseFloat(document.getElementById("c-dist").value);
 if(motoristaSelecionado===null) return alert("Escolhe um motorista primeiro");
 let pas=passageiros.find(x=>x.cpf==cpf); if(!pas) return alert("CPF não encontrado, cadastra antes");
 let mot=motoristas[motoristaSelecionado];
 let cor=new Corrida(pas,mot,ori,des,dist);
 mot.disponivel=false; mot.tempoRestante=cor.tempoTotalSeg();
 corridas.push(cor); corridasAtivas.push(cor); corridaAtual=cor;
 document.getElementById("msg-c").innerHTML=`<div style="background:#d4edda;padding:12px;border-radius:10px">✅ Indo pro mapa!</div>`;
 iniciarMapaCorrida(cor); aba("mapa");
}

// Faz o carrinho andar no mapa, essa parte é a mais legal
function iniciarMapaCorrida(corrida){
 if(!map) initMap(); 
 if(markerTaxi) map.removeLayer(markerTaxi); 
 if(rotaLine) map.removeLayer(rotaLine);
 let orig=getCoord(corrida.origem), dest=getCoord(corrida.destino);
 rotaLine=L.polyline([orig,dest],{color:'#153e84',weight:5,dashArray:'10,10'}).addTo(map);
 map.fitBounds([orig,dest],{padding:[50,50]});
 let taxiIcon=L.divIcon({className:'taxi',html:'🚕',iconSize:[40,40]});
 markerTaxi=L.marker(orig,{icon:taxiIcon}).addTo(map);
 L.marker(orig).addTo(map).bindPopup(`📍 Saída: ${corrida.origem}`).openPopup();
 L.marker(dest).addTo(map).bindPopup(`🏁 Destino: ${corrida.destino}`);
 document.getElementById("infoCorrida").innerHTML=`🚕 <b>${corrida.motorista.nome}</b> levando <b>${corrida.passageiro.nome}</b><br>📍 ${corrida.origem} → ${corrida.destino}`;
 let inicio=Date.now(), total=corrida.tempoTotalSeg()*1000;
 if(animInterval) clearInterval(animInterval);
 animInterval=setInterval(()=>{
   let elapsed=Date.now()-inicio, progress=Math.min(elapsed/total,1);
   let lat=orig[0]+(dest[0]-orig[0])*progress, lng=orig[1]+(dest[1]-orig[1])*progress;
   markerTaxi.setLatLng([lat,lng]); // aqui que o carro vai andando
   let restante=Math.ceil((total-elapsed)/1000);
   corrida.motorista.tempoRestante=restante>0?restante:0;
   document.getElementById("tempoMapa").textContent=restante>0?restante+"s":"Chegou! ✅";
   document.getElementById("valorMapa").textContent="R$ "+corrida.valor.toFixed(2);
   document.getElementById("progMapa").style.width=(progress*100)+"%";
   if(progress>=1){
     clearInterval(animInterval); 
     corrida.motorista.disponivel=true; // libera o motorista de novo
     corrida.status="finalizada";
     corridasAtivas=corridasAtivas.filter(c=>c!==corrida);
     document.getElementById("infoCorrida").innerHTML=`✅ Chegou em ${corrida.destino}! Motorista livre`;
     renderMotoristas(); renderHist();
   }
 },100);
}

function renderHist(){let div=document.getElementById("hist"); if(corridas.length==0){div.innerHTML="Nenhuma corrida ainda";return} div.innerHTML=corridas.slice().reverse().map((c,i)=>`<div class="card">${corridas.length-i} - ${c.passageiro.nome} com ${c.motorista.nome} ${c.status=="finalizada"?"✅":"⏳"} - R$ ${c.valor.toFixed(2)} - ${c.origem} → ${c.destino}</div>`).join("")}

// Faz o ENTER pular de campo, bem mais rápido pra usar
function ligarEnter(ids){
 ids.forEach((id,i)=>{
   let el=document.getElementById(id); if(!el) return;
   el.addEventListener("keydown",e=>{
     if(e.key==="Enter"){
       e.preventDefault();
       if(i<ids.length-1) document.getElementById(ids[i+1]).focus();
       else solicitar();
     }
   })
 })
}

// Quando abre o site já carrega tudo
window.onload=()=>{
 renderMotoristas(); calcPrev();
 ligarEnter(["m-nome","m-placa","m-tipo"]);
 ligarEnter(["p-nome","p-cpf"]);
 ligarEnter(["c-cpf","c-origem","c-destino","c-dist","c-tipo"]);
 document.getElementById("c-dist").addEventListener("input",calcPrev);
 document.getElementById("c-tipo").addEventListener("change",filtrarMotoristas);
}