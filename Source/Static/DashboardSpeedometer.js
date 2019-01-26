class Speedometer {

    constructor(speedometerCanvas, speedometerContainer) {
        this.canvas = document.getElementById(speedometerCanvas);
        this.canvas.width = $(speedometerContainer).width();
        this.canvas.height = $(speedometerContainer).height();

        this.context = this.canvas.getContext('2d');
        this.currentPercent = 0;
        this.textPercent = "0";

        this.currentSpeed = 0;
        this.textSpeed = "0";

        this.arcThreePos = 90;
        this.arcThreeIncrement = this.currentPercent * 10

        this.arcFourPos = 0;

        this.fontBase = this.canvas.width;                   // selected default width for canvas
        this.fontSize = 18;                     // default size for font
    }

    updateResize() {
        this.canvas.width = $(speedometerContainer).width();
        this.canvas.height = $(speedometerContainer).height();
        this.updateSpeedGauge();
    }

    updatePerpLine() {
        var radius = this.canvas.width/2 - 11
        var degrees = this.percentToDegrees(this.currentPercent)
        var radians = this.degreesToRadians(degrees)

        var x = Math.cos(radians) * radius + (this.canvas.width / 2);
        var y = Math.sin(radians) * radius + (this.canvas.height / 2);

        var innerX = (x + this.canvas.width / 2) * .5
        var innerY = (y + this.canvas.height / 2) * .5
        var innerX = (x + innerX) * .5
        var innerY = (y + innerY) * .5
        
        
        this.context.strokeStyle = "rgb(58,161,199)";
        this.context.lineWidth = 1;
        // this.context.shadowBlur = 100;
        // this.context.shadowColor = "rgb(58,161,199)";
        // this.context.shadowOffsetX = 0;
        // this.context.shadowOffsetY = 0;
        this.context.beginPath();
        this.context.moveTo(x,y)
        this.context.lineTo(innerX, innerY)
        this.context.stroke()

        // createRadialGradient()
        

        var grad = this.context.createRadialGradient(x,y,20,innerX,innerY,0);
        grad.addColorStop(0,"transparent");
        grad.addColorStop(1,"rgb(58,161,199)");
        
        this.context.fillStyle = grad;
        this.context.fillRect(0, 0, 150, 500);
    }
    
    updateBackDrop() {
        // console.log("enter")
        this.context.strokeStyle = "rgba(23,25,44, 0.5)";
        this.context.fillStyle = "rgba(0, 128, 255, 0.2)";
        // this.context.fillStyle = "rgb(255, 255, 255)";
        
        this.context.beginPath();
        
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2,0,2*Math.PI,false);
        
        this.context.stroke();
        this.context.closePath();
        this.context.fill();
    }

    getFont() {
        var ratio = this.fontSize / this.fontBase;   // calc ratio
        var size = this.canvas.width * ratio;   // get font size based on current width
        return (size|0) + 'px sans-serif'; // set font
    }

    updateTextGuage() {
        //(fontSize|0) + 'px myFont';
        // var fontSize = 
        // this.context.font = (fontSize|0) + "px Arial";
        this.context.font = this.getFont()
        this.context.textAlign = "center";
        this.context.fillStyle = "white"

        var percentage = this.textPercent
        percentage = percentage.toString() + "%"
        this.context.fillText(percentage, this.canvas.width/2, this.canvas.height/2-12.5);

        var speedInt = this.currentPercent * 70
        var speed = speedInt.toString().slice(0,4)
        if (speedInt < 10.0) {
            speed = "0" + speed
        }
        if (speed.length == 2) {
            speed += ".0"
        }
        speed = speed.slice(0,4)
        speed = speed + " km/h"

        this.context.fillText(speed, this.canvas.width/2, this.canvas.height/2+20);
    }

    updateArcPower() {
        var gradient = this.context.createLinearGradient((this.canvas.width)/2 - 80, 0, (this.canvas.width)/2 + 80, 0);
        gradient.addColorStop("0", "#017a09");
        gradient.addColorStop("0.5" ,"yellow");
        gradient.addColorStop("0.8" ,"yellow");
        gradient.addColorStop("1.0", "red");
        
        this.context.strokeStyle = gradient; 
        this.context.lineWidth = 4;
        
        var startDegrees = 150;
        var finishDegrees = this.percentToDegrees(100);
        var startRadians = this.degreesToRadians(startDegrees);
        var finishRadians = this.degreesToRadians(finishDegrees);
        this.context.beginPath();
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2-30,startRadians,finishRadians,false);
        this.context.stroke();
    }

    updateArcSpeed() {
        var gradient = this.context.createLinearGradient((this.canvas.width)/2 - 80, 0, (this.canvas.width)/2 + 80, 0);
        gradient.addColorStop("0", "#017a09");
        gradient.addColorStop("0.5" ,"yellow");
        gradient.addColorStop("0.8" ,"yellow");
        gradient.addColorStop("1.0", "red");
        
        this.context.strokeStyle = gradient; 
        this.context.lineWidth = 4;
        
        var startDegrees = 150;
        var finishDegrees = this.percentToDegrees(100);
        var startRadians = this.degreesToRadians(startDegrees);
        var finishRadians = this.degreesToRadians(finishDegrees);
        this.context.beginPath();
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2-40,startRadians,finishRadians,false);
        this.context.stroke();
    }

    updateArcPowerSheathPower() {
        //"rgb(58,161,199)"
        this.context.strokeStyle = "rgb(28,43,64)"; 
        this.context.lineWidth = 6;
        
        var startDegrees = 150;
        var finishDegrees;
        // if (this.currentPercent != 0) {
            // startDegrees = this.percentToDegrees(this.currentPercent)-5;

            finishDegrees = this.percentToDegrees(this.currentPercent);
        // }
        // else {
        //     startDegrees = 0;
        //     finishDegrees = 360;
        // }
        var startRadians = this.degreesToRadians(startDegrees);
        var finishRadians = this.degreesToRadians(finishDegrees);
        this.context.beginPath();
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2-30,startRadians,finishRadians,true);
        this.context.stroke();
    }

    updateArcPowerSheathSpeed() {
        //"rgb(58,161,199)"
        this.context.strokeStyle = "rgb(28,43,64)"; 
        this.context.lineWidth = 6;
        
        var startDegrees = 150;
        var finishDegrees;
        // if (this.currentPercent != 0) {
            // startDegrees = this.percentToDegrees(this.currentPercent)-5;

            finishDegrees = this.percentToDegrees(this.currentPercent);
        // }
        // else {
        //     startDegrees = 0;
        //     finishDegrees = 360;
        // }
        var startRadians = this.degreesToRadians(startDegrees);
        var finishRadians = this.degreesToRadians(finishDegrees);
        this.context.beginPath();
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2-40,startRadians,finishRadians,true);
        this.context.stroke();
    }

    updateArcPowerThree() {
        if (this.arcThreePos > 360) {
            this.arcThreePos -= 360;
        }

        this.arcThreeIncrement = this.currentPercent * 10;

        this.context.strokeStyle = "rgb(110, 154, 216)"; 
        this.context.lineWidth = 2;
        
        var startDegrees = this.arcThreePos-5;
        var finishDegrees = this.arcThreePos+5;
        var startRadians = this.degreesToRadians(startDegrees);
        var finishRadians = this.degreesToRadians(finishDegrees);
        
        this.context.beginPath();
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2-20,startRadians,finishRadians,true);
        this.context.stroke();
        
        this.arcThreePos += this.arcThreeIncrement;
    }

    updateArcPowerFour() {
        this.context.strokeStyle = "rgb(150,150,150)"; 
        this.context.lineWidth = 2;
        
        var startDegrees = this.arcFourPos
        var finishDegrees = this.arcFourPos + 360
        if (finishDegrees > 360) {
            finishDegrees -= 361;
        }
        // console.log(startDegrees, finishDegrees)
        
        var startRadians = this.degreesToRadians(startDegrees);
        var finishRadians = this.degreesToRadians(finishDegrees)
        


        this.context.beginPath();
        this.context.setLineDash([5, 5]);
        this.context.arc(this.canvas.width/2,this.canvas.height/2,this.canvas.width/2-10,startRadians,finishRadians,false);
        this.context.stroke();
        this.context.setLineDash([]);

        this.arcFourPos += this.arcThreeIncrement/2;
        if (this.arcFourPos > 360) {
            this.arcFourPos -= 360;
        }
    }

    updateSpeedGauge(percent = -5) {
        if (percent > 100) {
            return 0;
        }
        if (percent != -5) {
            var newPercentage = percent / 100;
            this.currentPercent = newPercentage;
        }
        
        // console.log(this.currentPercent)

        this.context.clearRect(0, 0, canvas.width, canvas.height);

        
        this.updateBackDrop();
        this.updateArcSpeed();
        this.updateArcPowerSheathSpeed();
        this.updateArcPower();
        this.updateArcPowerSheathPower();
        this.updateArcPowerThree();
        this.updateArcPowerFour();
        // this.updatePerpLine();
        this.updateTextGuage();

    }

    percentToDegrees(percentage) {
        return (percentage * 240) + 150;
    }

    degreesToRadians(degrees) {
        return degrees * (Math.PI/180);     
    }
    
    radiansToDegrees(radians) {
        return radians * (180/Math.PI);
    }

    updatePercent(percent) {
        this.textPercent = percent;
        this.currentPercent = percent/100;
    }
}

let speedometer = new Speedometer(speedometerCanvasId, speedometerContainerId)
speedometer.updatePercent(70);
speedometer.updateSpeedGauge();
// speedometer.updateArcPowerThree();


// var intervalFunction = speedometer.updateArcPowerThree();

function test() {
    speedometer.updateSpeedGauge();
}

setInterval(test, 50)
// setInterval( _.bind( function(){speedometer.updateArcPowerThree();}, this), 50);

var temp = 0;
function incSpeed() {
    // console.log(temp)
    if (temp <= 100) {
        speedometer.updatePercent(temp);
        temp += 1
    }
}

setInterval(incSpeed, 50);

$(window).bind('resize', function () {
    speedometer.updateResize();
}).trigger('resize');