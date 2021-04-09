let colorInput = document.querySelector('.color-input');
        var hueb = new Huebee(colorInput, {

            setBGColor: true,
            hue0: 0,
            hues: 1,
            shades: 0,
            customColors: ["#ffb3ba", "#ffdfba", "#ffffba", "#baffc9", "#bae1ff"],

        });
        hueb.on('change', function (color, hue, sat, lum) {
            document.getElementById("idea-form").style.backgroundColor = color;

        });