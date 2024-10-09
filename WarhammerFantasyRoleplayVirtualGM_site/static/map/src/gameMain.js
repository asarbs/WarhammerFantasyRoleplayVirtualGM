import { Application, Assets, Sprite, Graphics } from "http://127.0.0.1:8000/static/map/libs/pixijs_v8.4.1/pixi.mjs";

// Asynchronous IIFE
(async () =>
{
    const app = new Application();
    await app.init({ background: '#1099bb', resizeTo: window });
    document.body.appendChild(app.canvas);

    const texture = await Assets.load('http://127.0.0.1:8000/static/map/assets/bunny.png');
    const bunny = new Sprite(texture);
    app.stage.addChild(bunny);
    bunny.anchor.set(0.5);
    bunny.x = app.screen.width / 2;
    bunny.y = app.screen.height / 2;

    function moveSprite() {
        const speed = 5; // prędkość ruchu

        // Sprawdź, które klawisze są naciśnięte
        if (keys['w']) { // ruch w górę
            bunny.y -= speed;
        }
        if (keys['s']) { // ruch w dół
            bunny.y += speed;
        }
        if (keys['a']) { // ruch w lewo
            bunny.x -= speed;
        }
        if (keys['d']) { // ruch w prawo
            bunny.x += speed;
        }
    }

    // Obiekt do przechowywania stanu klawiszy
    const keys = {};

    // Nasłuchuj zdarzeń klawiatury
    window.addEventListener('keydown', (event) => {
        keys[event.key.toLowerCase()] = true; // ustawienie klawisza jako naciśnięty
    });

    window.addEventListener('keyup', (event) => {
        keys[event.key.toLowerCase()] = false; // ustawienie klawisza jako nie naciśnięty
    });

    app.ticker.add( () => { moveSprite(); });

})();