<?php
class ElectronicItem
{
    private $price;
    private $wired = false;
    private $extrasLimit;
    private $type;
    private $extras = array();
    
    const ELECTRONIC_ITEM_TELEVISION = 'television';
    const ELECTRONIC_ITEM_CONSOLE = 'console';
    const ELECTRONIC_ITEM_MICROWAVE = 'microwave';
    const ELECTRONIC_ITEM_CONTROLLER = 'controller';

    public function setPrice(float $price)
    {
        $this->price = $price;
    }

    public function getPrice(): float
    {
        return $this->price;
    }

    public function setType(string $type)
    {
        $this->type = $type;
    }

    public function getType(): string
    {
        return $this->type;
    }

    public function setWired(bool $wired)
    {
        $this->wired = $wired;
    }

    public function getWired(): bool
    {
        return $this->wired;
    }

    protected function maxExtras(int $max)
    {
        $this->extrasLimit = $max;
    }

    public function getLimit(): int
    {
        return $this->extrasLimit;
    }

    public function getExtras(): array
    {
        return $this->getExtras;
    }

    public function addExtras(...$args)
    {
        if (!$this->extrasLimit) {
            throw new Exception('Extras limit has not been set');
        }
        if ($this->extrasLimit === 0) {
            throw new Exception("Item { $this->getType() } can not have any extras");
        }

        if (sizeof($this->extras) + sizeof($args) > $this->extrasLimit) {
            throw new Exception('Extras to add exceeds max limit');
        }
         
        array_push($this->extras, ...$args);
    }
}

class Console extends ElectronicItem
{
    public function __construct()
    {

        $this->setType(ElectronicItem::ELECTRONIC_ITEM_CONSOLE);

        $this->maxExtras(4);
    }
}

class Television extends ElectronicItem
{
    public function __construct()
    {

        $this->setType(ElectronicItem::ELECTRONIC_ITEM_TELEVISION);
        
        $this->maxExtras(PHP_INT_MAX);
    }
}

class Microwave extends ElectronicItem
{
    public function __construct()
    {
        $this->setType(ElectronicItem::ELECTRONIC_ITEM_MICROWAVE);
        
        $this->maxExtras(0);
    }
}

class Controller extends ElectronicItem
{
    public function __construct()
    {
        $this->setType(ElectronicItem::ELECTRONIC_ITEM_CONTROLLER);
        $this->maxExtras(0);
    }
}

class Purchase
{
    private $items = array();
    public function __construct(...$items)
    {
        array_push($this->items, ...$items);
    }

    public function sortByPrice($desc = false)
    {
        usort($this->items, function ($item1, $item2) use ($desc) {
            $order = $item1->getPrice() > $item2->getPrice() ? 1 : -1;
            return $desc ? $order * -1 : $order;
        });
        return $this->items;
    }
    
    public function getTotal(): float
    {
        return array_reduce($this->items, function ($acc, $item) {
            return $acc + $item->getPrice();
        }, 0);
    }

    public function getItemsByType($type): array
    {
        return array_filter($this->items, function($item) use($type) {
            return $item->getType() == $type;
        });
    }
}

$console = new console();
$console->setPrice(999.98);
$controller1ForConsole = new Controller();
$controller2ForConsole = new Controller();
$controller3ForConsole = new Controller();
$controller3ForConsole->setWired(true);
$controller4ForConsole = new Controller();
$controller4ForConsole->setWired(true);
$console->addExtras($controller1ForConsole, $controller2ForConsole, $controller3ForConsole, $controller4ForConsole);

$tv1 = new Television();
$tv1->setPrice(499.99);
$controller1ForTv1 = new Controller();
$controller2ForTv1 = new Controller();
$tv1->addExtras($controller1ForTv1, $controller2ForTv1);

$tv2 = new Television();
$tv2->setPrice(799.97);
$controller1ForTv2 = new Controller();
$tv2->addExtras($controller1ForTv2);

$microwave = new Microwave();
$microwave->setPrice(189.99);

$purchase = new Purchase($console, $tv1, $tv2, $microwave);
$sortedItems = $purchase->sortByPrice();
var_dump($sortedItems);

// calcalute the total price
$total = $purchase->getTotal();
var_dump($total);

$consolesAsked = $purchase->getItemsByType(ElectronicItem::ELECTRONIC_ITEM_CONSOLE);
if (sizeof($consolesAsked)) {
    $firstConsole = array_values($consolesAsked)[0];
    echo $firstConsole->getPrice();
}
