const { Scene, PerspectiveCamera, Geometry, LineBasicMaterial, WireframeGeometry, DirectionalLight, OrbitControls, Color, AmbientLight, WebGLRenderer, BoxGeometry,
	MeshBasicMaterial, LineSegments, Mesh, OBJLoader, LoadingManager, Fog, BoxBufferGeometry, MeshNormalMaterial} = THREE 

let scene = new Scene();
scene.background = new Color( 0x26252a );
scene.fog = new Fog(0xffffff, 0.2, 10000)
let camera = new PerspectiveCamera( 60, window.innerWidth/window.innerHeight, 1, 10000 );

let renderer = new WebGLRenderer();
renderer.setPixelRatio( window.devicePixelRatio );

let controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.enableZoom = true;



let geometry = new BoxBufferGeometry( 100, 100, 100 );
let material = new MeshNormalMaterial();

let cubeMaterials = [ 
    new THREE.MeshBasicMaterial({color:0x2b2d2f, transparent:true, opacity:1, side: THREE.DoubleSide}),
    new THREE.MeshBasicMaterial({color:0x898989, transparent:true, opacity:1, side: THREE.DoubleSide}), 
    new THREE.MeshBasicMaterial({color:0xd3d3d3, transparent:true, opacity:1, side: THREE.DoubleSide}),
    new THREE.MeshBasicMaterial({color:0x808080, transparent:true, opacity:1, side: THREE.DoubleSide}), 
    new THREE.MeshBasicMaterial({color:0xaaafaa, transparent:true, opacity:1, side: THREE.DoubleSide}), 
    new THREE.MeshBasicMaterial({color:0xbfff00, transparent:true, opacity:1, side: THREE.DoubleSide}), 
]; 
var cubeMaterial = new THREE.MeshFaceMaterial(cubeMaterials); 


group = new THREE.Group();

for ( var i = 0; i < 300; i ++ ) {

	var mesh = new THREE.Mesh( geometry, cubeMaterial );
	mesh.position.x = Math.random() * 2000 - 1000;
	mesh.position.y = Math.random() * 2000 - 1000;
	mesh.position.z = Math.random() * 2000 - 1000;
	mesh.rotation.x = Math.random() * 2 * Math.PI;
	mesh.rotation.y = Math.random() * 2 * Math.PI;
	mesh.matrixAutoUpdate = false;
	mesh.updateMatrix();
	group.add( mesh );

}

scene.add( group );


renderer.setSize(window.innerWidth, window.innerHeight); // need to improve
window.addEventListener('resize', function() {
	renderer.setSize(window.innerWidth, window.innerHeight);
});

document.body.appendChild( renderer.domElement );


camera.position.z -= 500;

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}

let animate = function () {
	requestAnimationFrame( animate );
	controls.update();
	var time = Date.now() * 0.0001;
	let rx = Math.sin( time * 0.7 ) * 0.5;
	let ry = Math.cos( time * 0.3 ) * 0.5;
	let rz = Math.sin( time * 0.2 ) * 0.5;

	group.rotation.x = rx;
	group.rotation.y = ry;
	group.rotation.z = rz;

	renderer.render( scene, camera );
};

animate();	
